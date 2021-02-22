import numpy as np

#How to get the common items between two python numpy arrays?

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

res = np.intersect1d(a, b)
print(res)