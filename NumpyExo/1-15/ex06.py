import numpy as np

#Replace all odd numbers in arr with -1 without changing arr

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)
print(out)