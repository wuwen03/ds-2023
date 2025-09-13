def gcd(a:int,b:int) :
    if b==0:
        return a
    return gcd(b,a%b)

[x,y]=[int(i) for i in input("请输入两个数字:").split()]

print(gcd(x,y))