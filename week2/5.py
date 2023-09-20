
vis={}
def Root(c:int,st=1):
    g=st
    eps=0.000001
    round=0
    while abs(g*g-c)>eps:
        g=(g+c/g)/2
        round=round+1
    print("round:",round)
    vis[round]=1
    return g


c=int(input("输入:"))
for i in range(2,2001):
    print(Root(c,i))
    # Root(c,i)
# print(vis)