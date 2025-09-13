import numpy as np

def fun(x):
    return 9*x+8

x=np.random.uniform(-2,2,size=30)
y=fun(x)+np.random.normal(0,1)
print(y)