import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1/(1+np.exp(-x))

x=np.arange(-8,8,0.2)
y=sigmoid(x)

plt.plot(x,y)
plt.show()