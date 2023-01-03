from __future__ import print_function
import torch
import numpy as np
import os


os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def ch_fileW8(input, name, frag_bit):
  x = input.clone().cpu()

  data = x.contiguous().view(-1).detach().numpy()
  data = data*(2.**frag_bit)
  for i in range(len(data)):
    data[i] = int(data[i])
    if data[i] < 0:
      data[i] += 256

  f = open(name,'w')
  for i in range(int(len(data))):
    f.write('{:02X}\n'.format(int(data[i])))
  f.close()

  return 0

def out_ch_fileW8(input, name, frag_bit):
  x = input.clone().cpu()
  num_bits = 8
  num_int = 3
  qmin = -(2.**(num_int - 1))
  qmax = qmin + 2.**num_int - 1./(2.**(num_bits - num_int))
  scale = 1/(2.**(num_bits - num_int))
  x = x - torch.fmod(x,scale)
  x[x.le(qmin)] = qmin
  x[x.ge(qmax)] = qmax

  data = x.contiguous().view(-1).detach().numpy()
  data = data*(2.**frag_bit)
  for i in range(len(data)):
    data[i] = int(data[i])
    if data[i] < 0:
      data[i] += 256

  f = open(name,'w')
  for i in range(int(len(data))):
    f.write('{:02X}\n'.format(int(data[i])))
  f.close()

  return 0