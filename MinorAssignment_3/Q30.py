def product_of_digits(num):
    prod=1
    while num>0:
        digit=num%10
        prod*=digit
        num//=10
    return prod
user=int(input("Enter a number: "))
print("The product of its digit is: ",product_of_digits(user))