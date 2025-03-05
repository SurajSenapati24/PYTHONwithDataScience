import pandas as pd
L = ['Cry', 'Apple', 'Orange', 'Sky', 'Banana']
s=pd.Series(L)
vowels='aeiouAEIOU'
con=s[s.str.contains('|'.join(vowels),na=False)]
print(con)
st=s[s.str[0].str.upper().isin(list(vowels))]
print(st)