def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
    
user=int(input("Enter choice: (1 for additon, 2 for subtraction, 3 for multiplication, 4 for division): "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if user==1:
    print("Addition is: ",add(a,b))
elif user==2:
    print("Subtraction is: ", sub(a,b))
elif user==3:
    print("Multiplication is: ", mul(a,b))
elif user==4:
    if b==0:
        print("Division can't be performed as b=0")
    else:
        print(f"Division is: {div(a,b):.2f}")
else:
    print("Invalid choice!!")