import numpy as np

#4-Extract all odd numbers from arr
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
res = a[a % 2 == 1]
print(res)