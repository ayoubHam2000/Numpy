import numpy as np

#Convert a 1D array to a 2D array with 2 rows

a = np.arange(10)
a = a.reshape((2, -1))
print(a)