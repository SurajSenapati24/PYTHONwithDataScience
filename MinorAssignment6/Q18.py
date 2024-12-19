import numpy as np
import pandas as pd
array = np.random.randint(0, 100, size=(4, 4))
print(array)
df = pd.DataFrame(array)
print(df.iloc[:, 0])