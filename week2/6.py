
def Root(c:int,st=1):
    g=c/st
    eps=0.0000001
    round=0
    while abs(g*g-c)>eps:
        g=(g+c/g)/2
        round=round+1
    print(st,round)
    return g


c=int(input("输入:"))
print(Root(c,1))
print(Root(c,2))
print(Root(c,3))
