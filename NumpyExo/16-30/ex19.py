import numpy as np

#Reverse the columns of a 2D array arr.
arr = np.arange(9).reshape(3,3)

print(arr)
print(arr[:, ::-1])