import numpy as np

a=np.mat([[2,1],[4,5]])
x=np.linalg.eig(a)
print(x.eigenvalues)
print(x.eigenvectors)