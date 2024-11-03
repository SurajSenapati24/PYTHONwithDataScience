def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in input_string:
        if char not in punctuation:
            result += char
    return result
input_string = input("Enter a string: ")
print("String without punctuation:", remove_punctuation(input_string))
