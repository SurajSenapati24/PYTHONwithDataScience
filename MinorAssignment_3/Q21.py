def factorial(n):
    if n==0 or n==1:
        return 1
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
user=int(input("Enter a number: "))
print(factorial(user))