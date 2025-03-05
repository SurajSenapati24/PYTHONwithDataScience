def remove_vowels():
    s = input("Enter a String: ")
    out = ""
    for i in s:
        if i.lower() not in "aeiou": 
            out += i 
    return out

print("String without vowels:", remove_vowels())
