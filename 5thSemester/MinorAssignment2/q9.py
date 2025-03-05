user_input = input("Enter a number: ")

# Check if the input is a valid integer
if user_input.isdigit() or user_input[1:].isdigit():
    number = int(user_input)
    remainder = number % 5

    match remainder:
        case 0:
            print("The remainder is 0.")
        case 1:
            print("The remainder is 1.")
        case 2:
            print("The remainder is 2.")
        case 3:
            print("The remainder is 3.")
        case 4:
            print("The remainder is 4.")
else:
    print("Invalid input.")
