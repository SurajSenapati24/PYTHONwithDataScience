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

bnum = int(input("Enter a binary number: "))
print("Decimal number is: ", binaryToDecimal(bnum))
num = int(input("Enter a decimal number: "))
print("Binary number is: ", decimalToBinary(num))

