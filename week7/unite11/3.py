import numpy as np
from sklearn import linear_model
def fun(x):
    return 9*x+8

x=np.random.uniform(0,10,size=30)
# y=fun(x)+np.random.normal(0,1)
y=fun(x)
reg=linear_model.LinearRegression()
# reg.fit([[i,] for i in x],y)
reg.fit([[i] for i in x],y)
print(reg.coef_,reg.intercept_)