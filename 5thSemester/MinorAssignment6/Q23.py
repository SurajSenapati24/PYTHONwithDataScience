import pandas as pd
temperatures = pd.DataFrame({
    'Maxine': [3, 5, 4],
    'James': [1, 2, 3],
    'Amanda': [6, 8, 9]
})
print(temperatures)
temperatures = pd.DataFrame(
    {'Maxine': [3, 5, 4], 'James': [1, 2, 3], 'Amanda': [6, 8, 9]},
    index=['Morning', 'Afternoon', 'Evening']
)
print(temperatures)
print(temperatures['Maxine'])
print(temperatures.loc['Morning'])
print(temperatures.loc[['Morning', 'Evening']])
print(temperatures[['Amanda', 'Maxine']])
print(temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']])
print(temperatures.describe())
print(temperatures.T)
temperatures = temperatures.reindex(sorted(temperatures.columns), axis=1)
print(temperatures)