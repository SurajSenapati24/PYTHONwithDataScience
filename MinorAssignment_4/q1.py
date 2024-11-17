"""Write a Python program to create a list of size N and store the random values in it and find the sum
 and average."""
import random as r
def random_list(size,lower,upper):
    return [r.randint(lower,upper) for i in range(size)]

n=int(input("Enter the size of the list: "))
lower=int(input("Enter the lower bound for random"))
upper=int(input("Enter the upper bound"))
l=random_list(n,lower,upper)
print(l)