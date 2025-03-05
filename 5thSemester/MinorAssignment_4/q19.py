import copy
l=[['Shallow',2,3],[4,5,6]]
l1=copy.copy(l)
l2=copy.deepcopy(l)
l1[1][0]=8
l2[0]=[1,2,3]
l2[1]=['Deep',5,6]
print(f"Original: {l}")
print(f"Shallow: {l1}")
print(f"Deep: {l2}")