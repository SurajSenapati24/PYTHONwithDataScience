import numpy as np
def median(arr):
    return np.median(arr)

def mode(arr):
    return np.bincount(arr.flatten()).argmax()
a1=np.array([1,2,1,3,4,5])
a2=a1.reshape((3,2))
a3=a1.reshape([2,3])
print(median(a1))
print(mode(a1))
print(median(a2))
print(mode(a2))
print(median(a3))
print(mode(a3))