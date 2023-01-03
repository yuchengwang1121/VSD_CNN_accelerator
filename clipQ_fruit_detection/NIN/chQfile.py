from __future__ import print_function
import torch
import numpy as np
import os


os.environ["CUDA_VISIBLE_DEVICES"] = "1"


def ch_fileW8(input, name, frag_bit):
    x = input.clone().cpu()
    k = x.transpose(1, 0).transpose(2, 1)
    if(k.size(2) % 4 != 0):
        ze = torch.zeros(k.size(0), k.size(1), 4-k.size(2) % 4)
        k = torch.cat((k, ze), 2)
    data = k.contiguous().view(-1).detach().numpy()
    data = data*(2.**frag_bit)

    # Change data to positive int
    for i in range(len(data)):
        data[i] = int(data[i])
        if data[i] < 0:
            data[i] += 256

    # write the data into file with hex value
    f = open(name, 'w')
    for i in range(int(len(data)/4)):
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[4*i]), int(data[4*i+1]), int(data[4*i+2]), int(data[4*i+3])))
    if len(data) % 4 == 1:
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[len(data)-1]), 0, 0, 0))
    elif len(data) % 4 == 2:
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[len(data)-2]), int(data[len(data)-1]), 0, 0))
    elif len(data) % 4 == 3:
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[len(data)-3]), int(data[len(data)-2]), int(data[len(data)-1]), 0))
    f.close()
    return 0

def out_ch_fileW8(input, name, frag_bit):
    x = input.clone().cpu()
    num_bits = 8
    num_int = 3
    qmin = -(2.**(num_int - 1))
    qmax = qmin + 2.**num_int - 1./(2.**(num_bits - num_int))
    scale = 1/(2.**(num_bits - num_int))
    x = x - torch.fmod(x, scale)
    x[x.le(qmin)] = qmin
    x[x.ge(qmax)] = qmax

    k = x.transpose(1, 0).transpose(2, 1)
    if(k.size(2) % 4 != 0):
        ze = torch.zeros(k.size(0), k.size(1), 4-k.size(2) % 4)
        k = torch.cat((k, ze), 2)
    data = k.contiguous().view(-1).detach().numpy()
    data = data*(2.**frag_bit)


    for i in range(len(data)):
        data[i] = int(data[i])
        if data[i] < 0:
            data[i] += 256

    # write the data into file with hex value
    f = open(name, 'w')
    for i in range(int(len(data)/4)):
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[4*i]), int(data[4*i+1]), int(data[4*i+2]), int(data[4*i+3])))
    if len(data) % 4 == 1:
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[len(data)-1]), 0, 0, 0))
    elif len(data) % 4 == 2:
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[len(data)-2]), int(data[len(data)-1]), 0, 0))
    elif len(data) % 4 == 3:
        f.write('{:02X}\n{:02X}\n{:02X}\n{:02X}\n'.format(
            int(data[len(data)-3]), int(data[len(data)-2]), int(data[len(data)-1]), 0))
    f.close()
    return 0