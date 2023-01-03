from __future__ import print_function
import torch
import numpy as np
import os


os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def ch_fileW2_kernel_3x3(input, name):
    x = input.clone().cpu()
    data = x.contiguous().view(-1).detach().numpy()

    cnt = 0
    sum = 0
    f = open(name, 'w')
    for i in range(len(data)):
        sum = sum + (int(data[i]) << (2*cnt))

        if cnt == 8:
            f.write('{:05X}'.format(int(sum)))
            f.write('\n')
            cnt = 0
            sum = 0
        else:
            cnt = cnt + 1

    f.close()

    return 0

def ch_fileW2_kernel_1x1(input, name, input_ch):
    x = input.clone().cpu()
    data = x.contiguous().view(-1).detach().numpy()

    cnt = 0
    sum = 0
    f = open(name, 'w')
    for i in range(len(data)):
        sum = sum + (int(data[i]) << (2*cnt))

        if cnt == 8 or (i%input_ch == input_ch-1):
            f.write('{:05X}'.format(int(sum)))
            f.write('\n')
            cnt = 0
            sum = 0
        else:
            cnt = cnt + 1

    f.close()
    return 0