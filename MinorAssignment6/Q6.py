import numpy as np
a=2**np.arange(6)
a=a.reshape(2,3)
print("Original Array before flatten/ravel: ")
print(a)
a_f=a.flatten()
a_f[1]=34
print("Flattened a: ",a_f)
a_r=a.ravel()
a_r[2]=44
print("Ravelled a: ",a_r)
print("Original Array after flatten/ravel: ")
print(a)