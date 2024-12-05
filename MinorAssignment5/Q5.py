tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
#a) Check whether the dictionary contains the key ‘Canada’.
print(f"Contains 'Canada':{'Canada' in tlds}")
# b) Check whether the dictionary contains the key ‘France’.
print(f"Contains 'France':{'France' in tlds}")
# c) Iterate through the key-value pairs and display them in a two-column format.
print("\nCountry and TLD (Two-Column Format):")
for c, t in tlds.items():
    print(f"{c:15} {t}")
#d) Add the key–value pair ‘Sweden’ and ‘sw’ (incorrect TLD).
tlds['Sweden']='sw'
print(tlds)
# e) Update the value for the key ‘Sweden’ to ‘se’ (correct TLD).
tlds['Sweden']='se'
print(tlds)
# f) Use dictionary comprehension to reverse the keys and values.
tlds_rev={val:key for key,val in tlds.items()}
print(tlds_rev)