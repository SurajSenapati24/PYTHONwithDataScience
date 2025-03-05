import numpy as np
array = np.arange(1, 16).reshape(3, 5)
print(array)
print(array[2])
print(array[:, 4])
print(array[0:2])
print(array[:, 2:5])
print(array[1, 3])
print(array[1:3, [0, 2, 4]])