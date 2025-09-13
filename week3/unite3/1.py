x=float(input("输入的小数："))
a=int(x)
b=x-a
# print(a,b)
ans=""
while a:
    ans=str(a%2)+ans
    a//=2

if b:
    ans=ans+'.'
    cnt=100
    while b and cnt:
        b*=2
        if b>=1:
            ans=ans+'1'
            b-=1
        else:  
            ans=ans+'0'
        cnt-=1

print(ans)

