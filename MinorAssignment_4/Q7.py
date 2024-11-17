"""Write a function that takes a list of numbers as input from the user and produces the corresponding
 cumulative list where each element in the list at index i is the sum of elements at index j ≤ i."""
import random as r
def cumulative_list(l):
    cumulative=[]
    total=0
    for i in l:
        total+=i
        cumulative.append(total)
    return cumulative
l=[r.randint(1,30) for i in range(10)]
cum=cumulative_list(l)
print(l)
print(cum)