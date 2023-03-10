from torch.autograd import Variable
import torch



def valid(full, model, bin_op, validloader, criterion, epoch, load_acc):
    global best_acc
    model.eval()
    valid_loss = 0
    correct = 0
    if epoch==0:
        best_acc = load_acc
    if epoch==1:
        best_acc = 0
    if full == 0:
        bin_op.NbitClipQ()
    for data, target in validloader:
        data, target = Variable(data.cuda()), Variable(target.cuda())

        output = model(data)
        valid_loss += criterion(output, target).data.item()
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
    if full == 0:
        bin_op.restore()
    acc = 100. * float(correct) / len(validloader.dataset)
    # print("the acc is {} and the best is {}".format(acc, best_acc))
    if acc > best_acc:
        best_acc = acc
        save_state(model, best_acc)
    # print("After saving the acc is {} and the best is {}".format(acc, best_acc))

    valid_loss /= len(validloader.dataset)
    # print('\nThe epoch is: {}'.format(epoch))
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)'.format(
        valid_loss * 128., correct, len(validloader.dataset),
        100. * float(correct) / len(validloader.dataset)))
    print('Best Accuracy: {:.2f}%\n'.format(best_acc))
    return

def save_state(model, best_acc):
    print('==> Saving model ...')
    state = {
        'best_acc': best_acc,
        'state_dict': model.state_dict(),
    }
    for key in list(state['state_dict'].keys()):
        if 'module' in key:
            state['state_dict'][key.replace('module.', '')] = \
                state['state_dict'].pop(key)
    torch.save(state, 'NIN/nin_p.pth.tar')
