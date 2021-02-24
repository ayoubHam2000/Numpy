import numpy as np


#Import the iris dataset keeping the text intact.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype='object')
print(iris)



