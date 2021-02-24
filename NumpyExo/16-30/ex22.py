import numpy as np

#Pretty print rand_arr by suppressing the scientific notation (like 1e10)

# Create the random array
np.random.seed(0)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
#> array([[  5.434049e-04,   2.783694e-04,   4.245176e-04],
#>        [  8.447761e-04,   4.718856e-06,   1.215691e-04],
#>        [  6.707491e-04,   8.258528e-04,   1.367066e-04]])

#> array([[ 0.000543,  0.000278,  0.000425],
#>        [ 0.000845,  0.000005,  0.000122],
#>        [ 0.000671,  0.000826,  0.000137]])

#Sol

np.set_printoptions(suppress = True, precision = 6)
print(rand_arr)
