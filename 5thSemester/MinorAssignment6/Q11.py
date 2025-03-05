import numpy as np
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
print(np.vstack((array1, array2)))
print(np.hstack((array1, array2)))
print(np.vstack((np.hstack((array1, array2)), np.hstack((array1, array2)))))
print(np.hstack((np.vstack((array1, array2)), np.vstack((array1, array2)))))