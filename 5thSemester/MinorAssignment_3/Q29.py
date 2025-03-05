def is_perfect(num):
    divisor=[]
    for i in range(1,num//2+1):
        if num%i==0:
            divisor.append(i)
    s=sum(divisor)
    if s==num:
        return True
    else:
        return False
    
user=int(input("Enter a number: "))
print(f"Is the number perfect: {is_perfect(user)}")
