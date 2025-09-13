def root3(x):
    res=10
    count=1000
    while(abs(res*res*res-x)>1e-6 and count):
        res=res-(res*res*res-x)/(3*(res*res))
        count=count-1
        # print(res)
    return res


x=int(input("x:"))
print(root3(x))