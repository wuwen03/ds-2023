import random
def get_Pi1(round:int) -> float:
    within=0
    for i in range(0,round):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if x*x+y*y<=1:
            within=within+1
    return within/round*4

def get_Pi2(round:int) -> float:
    res=0
    for i in range(0,round):
        t=2*i+1
        if i%2==0:
            res=res+1/t
        else:
            res=res-1/t
    return res*4

def get_Pi3(round:int) :
    fac=[1]*(4*round+1)
    for i in range(2,4*round+1):
        fac[i]=fac[i-1]*i
    res=0
    for i in range(0,round):
        res=res+fac[4*i]*(1103+26390*i)/ ((fac[i]**4)*(396**(4*i)))
    res=res*2**1.5/99/99
    return 1/res
print(get_Pi1(1000000))
print(get_Pi2(1000000))
print(get_Pi3(1000))