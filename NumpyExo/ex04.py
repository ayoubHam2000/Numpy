import numpy as np

#4-Extract all odd numbers from arr
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = np.all(a % 2 == 1, axis = 0)
print(a)