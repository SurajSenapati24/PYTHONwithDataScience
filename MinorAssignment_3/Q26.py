def rep_vowels(str):
    vowels = "aeiouAEIOU"
    result = ""
    for char in str:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

user= input("Enter a string: ")
print("String after replacing vowels:", rep_vowels(user))
