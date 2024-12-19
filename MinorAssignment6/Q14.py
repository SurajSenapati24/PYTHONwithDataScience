import numpy as np
array = np.random.randint(0, 100, size=(5, 5))
bi=np.bincount(array.flatten())
print(bi)