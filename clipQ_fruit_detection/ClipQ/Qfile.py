from __future__ import print_function
import numpy as np
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def fileW8(input, name, frag_bit):
    d = input.clone().cpu()
    data = d.view(-1).detach().numpy()
    data = data*(2.**frag_bit)

    # Change data to positive int
    for i in range(len(data)):
        data[i] = int(data[i])
        if data[i] < 0:
            data[i] += 256

    # write the data into file with hex value
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