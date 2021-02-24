import numpy as np

#Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.



#Sol 1
rand_arr = np.random.randint(5, 10, size = (5, 3)) + np.random.rand(5, 3)

#Sol 2
rand_arr = np.random.rand(5, 3) * 5 + 5

#Sol 3
rand_arr = np.random.uniform(5, 10, size = (5, 3))

print(rand_arr)