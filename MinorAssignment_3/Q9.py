#Write two functions, one of which converts a binary number to decimal and the other one does the
#reverse.
def binaryToDecimal(num):
    pow = 0
    dec = 0
    while num > 0:
        digit = num % 10
        dec += digit * (2 ** pow)
        pow += 1
        num //= 10
    return dec
def decimalToBinary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        digit = num % 2
        binary = str(digit) + binary
        num //= 2
    return binary
user = int(input("Enter '1' to convert from binary to decimal and\n '2' to convert from decimal to binary: "))
if user == 1:
    num = int(input("Enter a binary number: "))
    print("Decimal number is: ", binaryToDecimal(num))
elif user == 2:
    num = int(input("Enter a decimal number: "))
    print("Binary number is: ", decimalToBinary(num))
else:
    print("Invalid input. Please enter 1 or 2.")
