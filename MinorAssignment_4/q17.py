import math
user=input("Enter 10 numbers: ")
lst=list(map(float,user.split()))
mean=sum(lst)/len(lst)
square_dif=[(x-mean)**2 for x in lst]
deviation=math.sqrt(sum(square_dif)/(len(lst)-1))
print(lst)
print(f"Mean: {mean:.2f}")
print(f"Deviation: {deviation:.2f}")
