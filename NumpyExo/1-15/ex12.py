import numpy as np

#From array a remove all items present in array b

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

res = np.setdiff1d(a, b)
print(res)