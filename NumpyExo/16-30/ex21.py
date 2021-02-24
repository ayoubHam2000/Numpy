import numpy as np

#Print or show only 3 decimal places(precision) of the numpy array rand_arr.

rand_arr = np.random.random((5,3))

np.set_printoptions(precision = 3)
print(rand_arr)