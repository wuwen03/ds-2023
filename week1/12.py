def root3(x):
    res=x/10000
    cnt=100000
    while(abs(res**3-x)>1e-20 and cnt):
        res=res-(res**3-x)/(3*(res**2))
        cnt=cnt-1
    return res


x=int(input("x:"))
print(root3(x))