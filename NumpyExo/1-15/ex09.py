import numpy as np

#Stack the arrays a and b horizontally.
a = np.arange(10).reshape(2,-1)

b = np.repeat(1, 10).reshape(2,-1)

print("a = ")
print(a)

print("b = ")
print(b)

#Method 1
res = np.hstack((a, b))

#Method 2
res = np.concatenate([a, b], axis = 1)

#Method 3
res = np.c_[a, b]

print("res = ")
print(res)