def remove_pun(str):
    pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in str:
        if char not in pun:
            result += char
    return result
str = input("Enter a string: ")
print("String without punctuation:", remove_pun(str))
