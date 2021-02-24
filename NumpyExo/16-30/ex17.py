import numpy as np

#Swap rows 1 and 2 in the array arr:

arr = np.arange(9).reshape(3,3)

print(arr)
arr = arr[[1, 0, 2], :]
print(arr)