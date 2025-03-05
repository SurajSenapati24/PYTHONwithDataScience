def is_armstrong(n):
    pow = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** pow
        temp //= 10
    return n == sum

user = int(input("Enter a number: "))
print(is_armstrong(user))
