import sys
import torchvision as tv
from torch.utils.data import random_split

def get_dataset(type):
    train_path = sys.path[0] + '/train'
    test_path = sys.path[0] + '/test'

    transform_img = tv.transforms.Compose([tv.transforms.ToTensor(),
                                              tv.transforms.Resize([32,32]),
                                              tv.transforms.Normalize((.5, .5, .5), (.5, .5, .5))])
    dataset = tv.datasets.ImageFolder(train_path, transform=transform_img)
    train_set_size = int(len(dataset) * 0.85)
    valid_set_size = len(dataset) - train_set_size

    # split dataset into train & valid ImgFolder (5306 & 1327)
    trainset, validset = random_split(dataset, (train_set_size, valid_set_size))

    if (type == 'train'):
        return trainset
    elif(type == 'valid'):
        return validset
    else:
        return tv.datasets.ImageFolder(test_path, transform=transform_img)
