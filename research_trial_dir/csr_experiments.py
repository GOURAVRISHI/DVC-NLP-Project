import numpy as np
from scipy.sparse import csr_matrix

A = np.array([
    [1,0,0,0,0,1,0],
    [0,1,0,3,0,0,0],
    [0,0,0,0,1,0,2],
])

print(A)


# matrix will save the values and ignore the number of zeroes
s= csr_matrix(A)
print(s)
print(type(s))

# converting them back to same format from sparse matrix
B=s.todense()
print(B)