import numpy as np

#Convert the function maxx that works on two scalars, to work on two arrays.

#region detail

'''
maxx(1, 5)
#> 5


Desired Output:
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max(a, b)
#> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])
'''

#endregion

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes = [float])

res = pair_max(a, b)

print(res)
    