from torch.autograd import Variable

def test(full, model, bin_op, testloader):
    model.eval()
    if full == 0:
        bin_op.NbitClipQ()

    withMask_cnt = 0
    withoutMask_cnt = 0

    for data, target in testloader:
        data, target = Variable(data.cuda()), Variable(target.cuda())

        output = model(data)
        pred = output.data.max(1, keepdim=True)[1]

        # print(pred)
        if(pred[0] == 0):
            print("[Result] With mask!")
            withMask_cnt += 1
        else:
            print("[Result] Without mask")
            withoutMask_cnt += 1

        print('WithMask: ', withMask_cnt,', withoutMask_cnt: ', withoutMask_cnt)

    if full == 0:
        bin_op.restore()

    return