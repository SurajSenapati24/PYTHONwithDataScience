from itertools import permutations
def unique_permutations(s):
    unique_perms = set(permutations(s))
    return [''.join(p) for p in unique_perms]

def palindrome_possible(s):
    perms = unique_permutations(s)
    for perm in perms:
        if perm == perm[::-1]: 
            return True
    return False
print(palindrome_possible("civic"))  
print(palindrome_possible("ivicc")) 
print(palindrome_possible("hello"))
print(palindrome_possible("aabb"))

