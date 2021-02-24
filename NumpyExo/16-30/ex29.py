import numpy as np

#Create a normalized form of iris's sepallength whose values range exactly between 0 and 1 
#so that the minimum has value 0 and maximum has value 1.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

Max = data.max()
Min = data.min()
N = (data - Min ) / (Max - Min)
print(N)