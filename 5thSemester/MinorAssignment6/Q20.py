import pandas as pd
s = pd.Series([1, 1, 3, 7, 88, 12, 88, 23, 3, 1, 9, 0])
print(s.idxmin()) 
print(s.idxmax())