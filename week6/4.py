import numpy as np
 

mat=np.mat([[2,-2],[1,-5]],dtype=float)
ans=np.mat([1,1])
print(np.linalg.eig(mat))

vec=np.mat([[0],[1]],dtype=float)
lam=0
for i in range(10000):
    y=mat.dot(vec)
    lam=y[np.argmax(np.abs(y))]
    vec=y/lam


print(vec)
print(lam)
