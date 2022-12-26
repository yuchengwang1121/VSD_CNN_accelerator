from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import torch
import argparse
import util
import util_write
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from data import get_dataset
# from models import nin
from torch.autograd import Variable

from torch.utils.data import random_split

if __name__ == '__main__':
    # prepare the options
    # set the seed
    # load fruit dataset
    train_loader = DataLoader(get_dataset("train"), batch_size=64, shuffle=True, num_workers=2)
    valid_loader = DataLoader(get_dataset("valid"), batch_size=64, shuffle=True, num_workers=2)
    test_loader = DataLoader(get_dataset("test"), batch_size=64, shuffle=True, num_workers=2)

    print(len(train_loader.dataset), " with ", len(valid_loader.dataset), " with ", len(test_loader.dataset))

