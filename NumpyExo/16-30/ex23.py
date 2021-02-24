import numpy as np

#Limit the number of items printed in python numpy array a to a maximum of 6 elements.

a = np.arange(30)
#> array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

#output
#> array([ 0,  1,  2, ..., 12, 13, 14])

np.set_printoptions(threshold = 4)
print(a)