"""Write a program to find the number of occurrences of each letter present in a given string., e.g.,
 str=‘mississippi’ ⇒ {‘m’: 1, ‘i’: 4, ‘s’: 4, ‘p’: 2}"""
str='mississippi'
d={}
for i in str:
    if i not in d:
        d[i]=str.count(i)
print(d)