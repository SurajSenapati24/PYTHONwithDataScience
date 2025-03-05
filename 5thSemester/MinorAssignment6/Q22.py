import pandas as pd
import numpy as np
a=pd.Series([7, 11, 13, 17])
print(a)
b=pd.Series([100.0] * 5)
print(b)
c = pd.Series(np.random.randint(0, 101, 20))
print(c.describe())
temperatures=pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures)
dictionary = dict(temperatures)
e=pd.Series(dictionary)
print(e)