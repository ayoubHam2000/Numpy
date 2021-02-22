import numpy as np

#Stack arrays a and b vertically

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

#Method 1
res = np.vstack([a, b])

#Method 2
res = np.r_[a, b]


#Method 3
res = np.concatenate([a, b], axis = 1)

print(res)
