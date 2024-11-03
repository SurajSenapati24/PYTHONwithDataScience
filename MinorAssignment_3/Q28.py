def shift_letters(input_string):
    result = ""
    for char in input_string:
        if char == 'z':  # Wrap 'z' to 'a'
            result += 'a'
        else:
            result += chr(ord(char) + 1)  # Shift other characters by one
    return result

input_string = input("Enter a string of lowercase alphabets: ")
print("Shifted string:", shift_letters(input_string))
