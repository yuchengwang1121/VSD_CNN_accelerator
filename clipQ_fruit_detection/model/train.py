from torch.autograd import Variable

def train(epoch, full, model, bin_op, trainloader, criterion, optimizer):
    model.train()
    for batch_idx, (data, target) in enumerate(trainloader):
        # process the weights including binarization
        if full == 0:
            bin_op.NbitClipQ()

        # forwarding
        data, target = Variable(data.cuda()), Variable(target.cuda())
        # print("The data is", data, " \n And the target is", target)
        optimizer.zero_grad()
        output = model(data)        # equel to model.forward(data)
        # print("the out is ", output, "\n the target is ", target)

        # backwarding
        loss = criterion(output, target)    # [64,33] & [64]
        loss.backward()

        # restore weights
        if full == 0:
            bin_op.restore()

        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}\tLR: {}'.format(
                epoch, batch_idx * len(data), len(trainloader.dataset),
                100. * batch_idx / len(trainloader), loss.data.item(),
                optimizer.param_groups[0]['lr']))
    return

def adjust_learning_rate(optimizer, epoch, max):
    e = int(max/5)
    update_list = [e, e*2, e*3, e*4]
    if epoch in update_list:
        for param_group in optimizer.param_groups:
            param_group['lr'] = param_group['lr'] * 0.1
    return