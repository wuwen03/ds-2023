c=int(input("输入："))
h=0.0000001
g=c/2
while abs(g*g-c)>0.000001:
    g=g+h
print(g)