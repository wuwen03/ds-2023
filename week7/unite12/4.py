import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import torch.nn.functional as F
from torch.utils.data import TensorDataset,DataLoader
from torch import optim,torch
iris_data = load_iris()
X = iris_data["data"]
Y = iris_data["target"]
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.7, random_state=20, shuffle=True
)
x_train=torch.tensor(x_train,dtype=torch.double)
x_test=torch.tensor(x_test,dtype=torch.double)
y_train=torch.tensor(y_train,dtype=torch.long)
y_test=torch.tensor(y_test,dtype=torch.long)

train_ds=TensorDataset(x_train,y_train)
train_dl=DataLoader(train_ds,batch_size=10)
test_ds=TensorDataset(x_test,y_test)
test_dl=DataLoader(test_ds,batch_size=10*2)

class Net(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.hidden=torch.nn.Linear(4,20,dtype=torch.double)
        self.out=torch.nn.Linear(20,3,dtype=torch.double)
    
    def forward(self,x):
        return self.out(F.relu(self.hidden(x)))

def get_model():
    model=Net()
    return model,optim.SGD(model.parameters(),lr=0.02)
    
model,opt=get_model()
loss_func=F.cross_entropy

epochs=50
for epoch in range(epochs):
    model.train()
    for xb,yb in train_dl:
        pred=model(xb)
        loss=loss_func(pred,yb)
        # print(loss)
        loss.backward()
        opt.step()
        opt.zero_grad()
        model.eval()
        with torch.no_grad():
            valid_loss = sum(loss_func(model(xb), yb) for xb, yb in test_dl)

    print(epoch, valid_loss / len(test_dl))
    with torch.no_grad():
        print(sum([np.argmax(model(xb))==yb for xb,yb in zip(x_train,y_train)]),len(x_train))

