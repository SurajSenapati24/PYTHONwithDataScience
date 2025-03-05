"""Write a Python program to create a list of size N and store the random values in it and find the sum
 and average."""
import random as r
n=int(input("Enter the size of the list: "))
l=[r.randrange(1,50) for _ in range(n)]
s=sum(l)
print(l)
print("Sum: ",s)
print("Average: ",s/n)