from __future__ import print_function
import numpy as np
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def fileW8(input, name, frag_bit):
    d = input.clone().cpu()
    data = d.view(-1).detach().numpy()
    data = data*(2.**frag_bit)
    for i in range(len(data)):
        data[i] = int(data[i])
        if data[i] < 0:
            data[i] += 256
    out = []
    for i in range(len(data)):
        out.append(hex(int(data[i])))
    f = open(name, 'w')
    for i in range(int(len(data)/4)):
        f.write('{:02X}{:02X}{:02X}{:02X}\n'.format(
            int(data[4*i]), int(data[4*i+1]), int(data[4*i+2]), int(data[4*i+3])))
    if len(data) % 4 == 1:
        f.write('{:02X}{:02X}{:02X}{:02X}\n'.format(
            int(data[len(data)-1]), 0, 0, 0))
    elif len(data) % 4 == 2:
        f.write('{:02X}{:02X}{:02X}{:02X}\n'.format(
            int(data[len(data)-2]), int(data[len(data)-1]), 0, 0))
    elif len(data) % 4 == 3:
        f.write('{:02X}{:02X}{:02X}{:02X}\n'.format(
            int(data[len(data)-3]), int(data[len(data)-2]), int(data[len(data)-1]), 0))
    f.close()
    return 0


def fileW32(input, name, frag_bit):
    d = input.clone().cpu()
    data = d.view(-1).detach().numpy()
    data = data*(2.**frag_bit)
    f = open(name, 'w')
    for i in range(int(len(data))):
        if data[i] < 0:
            data[i] = data[i] + 2**20
            if ('{:05X}'.format(int(data[i]))) == '100000':
                f.write('00000000\n')
            else:
                f.write('FFF{:05X}\n'.format(int(data[i])))
        else:
            f.write('{:08X}\n'.format(int(data[i])))
    f.close()

    return 0


def fileW2(input, name):
    d = input.clone().cpu()
    data = d.view(-1).detach().numpy()
    for i in range(len(data)):
        data[i] = int(data[i])

    if len(data) % 16 != 0:
        for i in range(16 - int(len(data) % 16)):
            data = np.append(data, [0])
    f = open(name, 'w')
    for i in range(int(len(data)/4)):
        num = data[4*i]*64 + data[4*i+1]*16 + data[4*i+2]*4 + data[4*i+3]
        f.write('{:02X}'.format(int(num)))

        if i % 4 == 3:
            f.write('\n')
    f.close()
    return 0