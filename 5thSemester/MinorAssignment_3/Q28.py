def shift_letters(str):
    result = ""
    for char in str:
        if char == 'z':  # Wrap 'z' to 'a'
            result += 'a'
        else:
            result += chr(ord(char) + 1)  # Shift other characters by one
    return result

str = input("Enter a string of lowercase alphabets: ")
print("Shifted string:", shift_letters(str))
