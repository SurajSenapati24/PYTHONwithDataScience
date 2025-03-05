"""Write a function that takes a list of numbers as input from the user and produces the corresponding
 cumulative list where each element in the list at index i is the sum of elements at index j ≤ i."""
def cumulative_list(l):
    cumulative=[]
    total=0
    for i in l:
        total+=i
        cumulative.append(total)
    return cumulative
l=[]
n=int(input("Enter the size of list: "))
for i in range(n):
    user=int(input("Enter a number: "))
    l.append(user)
cum=cumulative_list(l)
print(l)
print(cum)