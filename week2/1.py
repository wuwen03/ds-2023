n=int(input())
inf=1e9
dp=[-1]*(n+1)
pre=[-1]*(n+1)
# print(dp)
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=3
pre[1]=1
pre[2]=2
pre[3]=3
def rec(x:int)->int:
    if dp[x]!=-1:
        return dp[x]
    for i in range(1,x):
        l=rec(i)
        r=rec(x-i)
        if l*r>dp[x]:
            dp[x]=l*r
            pre[x]=l
    return dp[x]

rec(n)
# print(dp)
# print(pre)
now=n
ans=[]
while now:
    # print(pre[now])
    ans.append(pre[now])
    now=now-pre[now]
print(ans)

ans.clear()
if n%3==0:
    ans=ans+([3]*(n//3))
elif n%3==1:
    ans.append(4)
    ans=ans+([3]*((n-4)//3))
else:
    ans.append(2)
    ans=ans+([3]*((n-2)//3))
print(ans)
