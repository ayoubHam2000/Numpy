import numpy as np


#Find the mean, median, standard deviation of iris's sepallength (1st column)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter = ',', dtype = 'float', usecols = [0, 1, 2, 3])

print(np.mean(data[:, 0]))
print(np.median(data[:, 0]))
print(np.std(data[:, 0]))

#mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)

