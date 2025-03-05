"""For the following dictionary, create lists of its keys, values, and items, and show those lists.
 roman numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}"""
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}
keys=[_ for _ in roman_numerals.keys()]
vals=[_ for _ in roman_numerals.values()]
items=[_ for _ in roman_numerals.items()]
print("Keys: ",keys)
print("Values: ",vals)
print("Items: ",items)
