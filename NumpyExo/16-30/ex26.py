import numpy as np

#Extract the text column species from the 1D iris imported in previous question.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype='object')
iris_1d = iris.reshape(iris.shape[0] * iris.shape[1])
#print(iris_1d)


#species = np.array([row[4] for row in iris])
species = iris_1d[4::5]
print(species)


