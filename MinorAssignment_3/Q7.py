def check_alphabet(a):
    a.lower()
    if len(a)==1:
        if(a in "aeiou"):
            return "vowel"
        else:
            return "consonant"
    else:
        return "Not an alphabet!!"
user=input("Enter a alphabet: ")
print(check_alphabet(user))
