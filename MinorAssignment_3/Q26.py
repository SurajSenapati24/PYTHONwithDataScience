def replace_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

user= input("Enter a string: ")
print("String after replacing vowels:", replace_vowels(user))
