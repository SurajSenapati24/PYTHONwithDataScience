n=int(input("Enter a four digit number: "))
if n>999 and n<10000:
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    print("Sum of digits is: ",sum)
else:
    print("Please enter a four digit number")