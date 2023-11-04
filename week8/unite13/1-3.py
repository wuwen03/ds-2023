import torch
import torch.nn as nn
import torchvision
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#第1题
iris=load_iris()
X=iris['data']
Y=iris['target']
# print(iris)
# print(X[:,0:1])
for i in range(4):
    for j in range(i+1,4):
        plt.clf()
        plt.scatter(X[:,i],X[:,j])
        plt.savefig('./1/{}-{}.png'.format(i,j))
        # plt.show()

#第2题
iris_dataset=load_iris()
X=iris_dataset['data']
Y=iris_dataset['target']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.8,random_state=20,shuffle=True)

#第3题
from sklearn import neighbors
knn=neighbors.KNeighborsClassifier(3)
knn.fit(x_train,y_train)
print(knn.score(x_test,y_test))