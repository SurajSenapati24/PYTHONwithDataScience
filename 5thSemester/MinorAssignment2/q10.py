# Prompt user for input
user_input = input("Enter a string: ")

# Find and display all substrings
print("Substrings:")
for i in range(len(user_input)):
    for j in range(i + 1, len(user_input) + 1):
        print(user_input[i:j], end=" ")
