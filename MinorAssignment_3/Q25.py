def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(n1, n2):
    return gcd(n1, n2) == 1

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if are_coprime(n1, n2):
    print(f"{n1} and {n2} are coprime.")
else:
    print(f"{n1} and {n2} are not coprime.")
