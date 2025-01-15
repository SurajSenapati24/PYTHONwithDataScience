# Open the file in read mode
with open('sample.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
print(f"The number of words in the file is: {word_count}")
