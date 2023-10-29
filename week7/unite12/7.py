import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import torch.nn.functional as F
from torch.utils.data import TensorDataset,DataLoader
from torch import optim,torch
import pickle

class LeNet5(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cov1=torch.nn.Conv2d(1,6,5)
        self.pool1=torch.nn.AvgPool2d(2,2)
        self.cov2=torch.nn.Conv2d(6,16,5)
        self.pool2=torch.nn.AvgPool2d(2,2)
        self.fc1=torch.nn.Linear(16*4*4,120)
        self.fc2=torch.nn.Linear(120,84)
        self.fc3=torch.nn.Linear(84,10)
    
    def forward(self,x):
        x=x.view(-1,1,28,28)
        x=self.pool1(F.relu(self.cov1(x)))
        x=self.pool2(F.relu(self.cov2(x)))
        x=x.view(-1,16*4*4)
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=self.fc3(x)
        return x        

def get_model():
    model=LeNet5()
    return model,torch.optim.SGD(model.parameters(),lr=0.2)

dev = torch.device(
    "cuda") if torch.cuda.is_available() else torch.device("cpu")

model,opt=get_model()
loss_func=F.cross_entropy

from pathlib import Path
import requests

DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"

PATH.mkdir(parents=True, exist_ok=True)

URL = "https://github.com/pytorch/tutorials/raw/main/_static/"
FILENAME = "mnist.pkl.gz"

if not (PATH / FILENAME).exists():
        content = requests.get(URL + FILENAME).content
        (PATH / FILENAME).open("wb").write(content)

import pickle
import gzip

with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")

x_train,y_train,x_valid,y_valid=map(torch.tensor,(x_train,y_train,x_valid,y_valid))
x_train=x_train.to(dev)
y_train=y_train.to(dev)
x_valid=x_valid.to(dev)
y_valid=y_valid.to(dev)


train_ds=TensorDataset(x_train,y_train)
valid_ds=TensorDataset(x_valid,y_valid)
train_dl=DataLoader(train_ds,batch_size=50,shuffle=True)
valid_dl=DataLoader(valid_ds,batch_size=20)

model=model.to(dev)

epochs=10
for epoch in range(epochs):
    for xb,yb in train_dl:
        # print(xb.shape)
        pred=model(xb)
        loss=loss_func(pred,yb)

        loss.backward()
        opt.step()
        opt.zero_grad()
    print(epoch,loss)
with torch.no_grad():
    print(epoch,sum([np.argmax(model(xb).cpu())==yb for xb,yb in valid_ds]),len(valid_ds))
        


