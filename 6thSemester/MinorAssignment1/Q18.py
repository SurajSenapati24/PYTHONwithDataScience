import pandas as pd 
import matplotlib.pyplot as plt 
to_kelvin = lambda c: c + 273.15 
data = {'Celsius': list(range(0, 101, 10))} 
data['Kelvin'] = list(map(to_kelvin, data['Celsius'])) 
df = pd.DataFrame(data) 
df.plot(x='Celsius', y='Kelvin', kind='line') 
plt.show()