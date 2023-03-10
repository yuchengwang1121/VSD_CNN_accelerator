from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch
import argparse
import ClipQ.util as util
import ClipQ.util_write as util_write
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from NIN import nin
from data import get_dataset
from model.train import train, adjust_learning_rate
from model.valid import valid
from model.test import test
from parser_argu import init_parse

if __name__ == '__main__':
    # set the seed
    torch.manual_seed(1)
    torch.cuda.manual_seed(1)
    # load fruit dataset
    train_loader = DataLoader(get_dataset("train"), batch_size=64, shuffle=True, num_workers=2)
    valid_loader = DataLoader(get_dataset("valid"), batch_size=64, shuffle=True, num_workers=2)
    test_loader = DataLoader(get_dataset("test"), batch_size=64, shuffle=True, num_workers=2)

    # define classes
    classes = { 'Apple Braeburn', 'Apricot', 'Banana','Blueberry', 'Cherry', 
                'Cucumber Ripe', 'Grape Blue', 'Kiwi', 'Lemon', 'Limes', 
                'Mango', 'Onion White', 'Orange', 'Passion Fruit', 'Pepper Red',
                'Pineapple', 'Potato Red', 'Strawberry', 'Tomato', 'Watermelon'}

    # prepare the options
    parser = argparse.ArgumentParser()
    args = init_parse(parser).parse_args()
    print('==> Options:', args)

    # define the model
    full_p = int(args.full)
    print('==> building model', args.arch, '...')
    if args.arch == 'nin':
        model = nin.Net(f=full_p, write=args.write)
    else:
        raise Exception(args.arch+' is currently not supported')

    # initialize the model
    if not args.pretrained:
        print('==> Initializing model parameters ...')

        for m in model.modules():
            if isinstance(m, nn.Conv2d):
                m.weight.data.normal_(0, 0.05)
                m.bias.data.zero_()
    else:
        print('==> Load pretrained model form', args.pretrained, '...')
        pretrained_model = torch.load(args.pretrained)
        model.load_state_dict(pretrained_model['state_dict'])

    # chose device as CPU or GPU
    if not args.cpu:
        model.cuda()
        model = torch.nn.DataParallel(model, device_ids=range(torch.cuda.device_count()))

    # print(model)   //UnComment out for the structure of the nin model

    # define solver and criterion
    base_lr = float(args.lr)
    param_dict = dict(model.named_parameters())
    params = []

    for key, value in param_dict.items():
        params += [{'params': [value], 'lr': base_lr,
                    'weight_decay':0.00001}]
    if args.opt == 'Adam':
        optimizer = optim.Adam(params, lr=0.001, weight_decay=0.00001)
    else:
        optimizer = optim.SGD(params, lr=0.001, weight_decay=0.00001)

    criterion = nn.CrossEntropyLoss()

    # define the binarization operator
    if args.write and args.evaluate:
        bin_op = util_write.Quantize(model)
    else:
        bin_op = util.Quantize(model)

    load_acc = 0
    # predict single picture
    if args.predict:
        load_acc = pretrained_model['best_acc']
        test(full_p,model, bin_op, test_loader)
        exit(0)

    # do the evaluation if specified
    if args.evaluate:
        load_acc = pretrained_model['best_acc']
        valid(full_p, model, bin_op, valid_loader, criterion, 0, load_acc)
        exit(0)

    max_ep = int(args.epoch)
    # start training
    # print("start training")
    for epoch in range(1, max_ep):
        adjust_learning_rate(optimizer, epoch, max_ep)
        train(epoch, full_p, model, bin_op, train_loader, criterion, optimizer)
        valid(full_p, model, bin_op, valid_loader, criterion, epoch, 0)
        
