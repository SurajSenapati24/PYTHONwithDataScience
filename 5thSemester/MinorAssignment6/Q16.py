import numpy as np
arr1 = np.random.randint(0, 100, size=(9, 9, 2))
arr2=arr1[:5, :5, :]
print(arr1)
print(arr2.shape)