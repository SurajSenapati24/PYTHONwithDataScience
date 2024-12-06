s1 = {'red', 'green', 'blue'}
s2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

print("Comparison operators:")
print("Equal:", s1 == s2)
print("Not equal:", s1 != s2)
print("Subset:", s1 < s2)
print("Subset or equal:", s1 <= s2)
print("Superset:", s1 > s2)
print("Superset or equal:", s1 >= s2)

print("\nMathematical set operators:")
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)
print("Symmetric difference:", s1 ^ s2)
