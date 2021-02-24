import numpy as np

#Reverse the rows of a 2D array arr.

#Sol 1
arr = np.arange(12).reshape(4, 3)
print(arr)
arr = arr[::-1]
print(arr)

#Sol 2
arr = np.arange(12).reshape(4, 3)
#print(arr)
m = np.arange(arr.shape[0] - 1, -1, -1)
arr = arr[m, :]
#print(arr)