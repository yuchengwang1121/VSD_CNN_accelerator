from __future__ import print_function
import numpy as np
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def fileW32(input, name, frag_bit):
    d = input.clone().cpu()
    data = d.view(-1).detach().numpy()
    data = data*(2.**frag_bit)

    # write the data into file with hex value
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