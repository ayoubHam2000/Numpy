import numpy as np


#Compute the softmax score of data.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

def softmax(x) :
    return np.exp(x) / sum(np.exp(x))

print(softmax(data))