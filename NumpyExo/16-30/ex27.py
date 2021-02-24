import numpy as np

#Convert the 1D iris to 2D array iris_2d by omitting the species text field.

'''
Parameters
order{‘C’, ‘F’, ‘A’, ‘K’}, optional
‘C’ means to flatten in row-major (C-style) order. 
‘F’ means to flatten in column-major (Fortran- style) order. 
‘A’ means to flatten in column-major order if a is Fortran contiguous in memory, row-major order otherwise. 
‘K’ means to flatten a in the order the elements occur in memory. 
The default is ‘C’.
'''

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#Sol 1
iris = np.genfromtxt(url, delimiter=',', dtype='object')
iris1D = iris.flatten()

res = iris1D.reshape(-1, 5)
res = res[:, 0:4]

#Sol2
iris = np.genfromtxt(url, delimiter=',', dtype='object', usecols=[0, 1, 2, 3])


print(res)