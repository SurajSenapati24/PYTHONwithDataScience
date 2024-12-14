import numpy as np
a=2**np.arange(6)
a=a.reshape(2,3)
print(a)
a_f=a.flatten()
print("Flattened a: ",a_f)
a_r=a.ravel()
print("Ravelled a: ",a_r)