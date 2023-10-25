import numpy as np

a=np.array([[1,-1,4],[2,1,3],[1,3,-1]],dtype=float)
cov_mat=np.cov(a)
print(cov_mat)

print(np.linalg.eig(cov_mat))

vec=np.mat([[0],[0],[1]],dtype=float)
lam=0
for i in range(100000):
    y=cov_mat.dot(vec)
    lam=y[np.argmax(np.abs(y))][0]
    vec=y/lam


print(vec)
print(lam)
#好像采用幂迭代法只能够求出最大的特征值