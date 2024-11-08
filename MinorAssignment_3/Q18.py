def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if is_anagram(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
