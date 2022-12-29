from torch.autograd import Variable
import random

def test(full, model, bin_op, testloader):
    model.eval()
    if full == 0:
        bin_op.NbitClipQ()

    for data, target in testloader:
        data, target = Variable(data.cuda()), Variable(target.cuda())

        output = model(data)
        pred = output.data.max(1, keepdim=True)[1]

        # Choose one picture in the testloader
        index = int(random.uniform(0, target.size(dim=0)))
        if(target[index] == pred[index]):
            print("The chosen data {} is perdict correctly".format(index))
            break
        else:
            print("The chosen data {} is perdict wrong".format(index))

    if full == 0:
        bin_op.restore()

    return