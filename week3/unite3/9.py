import random
N=int(input("N:"))
A=[random.randint(1,10) for i in range(N)]
print(A)

pre=A.copy()
for i in range(1,N):
    pre[i]=pre[i]*pre[i-1]

post=A.copy()
for i in range(N-2,-1,-1):
    post[i]=post[i]*post[i+1]

B=[0 for i in range(N)]
for i in range(N):
    if i==0:
        B[i]=post[i+1]
    elif i==N-1:
        B[i]=pre[i-1]
    else:
        B[i]=pre[i-1]*post[i+1]

print(B)