import math
import random
def fun(x):
    return x*x+4*x*math.sin(x)

def Mont(round=1000):
    count=0
    for i in range(0,round):
        x=random.uniform(2,3)
        y=random.uniform(10,14)
        if 0<=y and y<=fun(x):
            count+=1
        elif fun(x)<=y and  y<=0:
            count-=1
    return 4*count/round+10

print(Mont(5000000))
            
