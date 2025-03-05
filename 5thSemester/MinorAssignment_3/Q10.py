from itertools import permutations as p

def unique_permutations(s):
    unique_perms = set(p(s))
    return [''.join(p) for p in unique_perms]
user = input("Enter a string: ")
print(unique_permutations(user))
