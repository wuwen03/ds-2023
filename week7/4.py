import numpy as np
from sklearn import linear_model

def fun(x):
    return np.sin(x)
x=np.random.uniform(-10,10,30)
y=fun(x)+np.random.normal(0,1)

reg=linear_model.LinearRegression()
reg.fit([[i] for i in x],y)
print(reg.coef_)