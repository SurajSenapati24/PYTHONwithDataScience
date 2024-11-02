from itertools import permutations

def unique_permutations(s):
    unique_perms = set(permutations(s))
    return [''.join(p) for p in unique_perms]
user = input("Enter a string: ")
print(unique_permutations(user))
