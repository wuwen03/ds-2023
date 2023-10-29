import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import torch.nn.functional as F
from torch.utils.data import TensorDataset,DataLoader
from torch import optim,torch
from PIL import Image
import torchvision


pic=Image.open('saber.png')
pic=torchvision.transforms.ToTensor()(pic)
cov1=torch.nn.Conv2d(4,1,(1,1))
cov1.weight.data=torch.Tensor([[[[0.25]],
                                [[0.25]],
                                [[0.25]],
                                [[0.25]]]])
cov1.bias.data=torch.Tensor([0])
pic=cov1(pic)
pic=torchvision.transforms.ToPILImage()(pic)
# pic.save("grey.png")


k=int(input("缩小k倍:"))
pic=Image.open('saber.png')
pic=torchvision.transforms.ToTensor()(pic)
pool=torch.nn.MaxPool2d((11,11),k,padding=5)
pic=pool(pic)
pic=torchvision.transforms.ToPILImage()(pic)
pic.save("smaller.png")

