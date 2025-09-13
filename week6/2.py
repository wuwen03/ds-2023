import matplotlib.pyplot as plt
import numpy.random as rd

x=[i for i in range(1,101)]
y=rd.normal(loc=0,scale=1,size=10000)
plt.hist(y,50)
plt.show()