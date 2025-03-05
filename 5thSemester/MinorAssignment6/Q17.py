import numpy as np
array = np.random.randint(0, 100, size=(4, 4))
print(array)
sarr=np.sort(array, axis=0)
print(sarr)