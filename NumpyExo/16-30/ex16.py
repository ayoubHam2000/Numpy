import numpy as np

#Swap columns 1 and 2 in the array arr.

#Sol 1
arr = np.arange(9).reshape(3,3)
print(arr)
arr = arr[:, [1, 0, 2]]
print(arr)

#Sol 2
arr = np.arange(9).reshape(3,3)
#print(arr)
temp = arr[:, 1]
arr[:, 1] = arr[:, 2]
arr[:, 2] = temp
#print(arr)