"""Write a function that takes n as an input and creates a list of n lists such that ith list contains the first
 five multiples of i"""
def generate_multiples(n):
    multiple_list=[]
    for i in range(1,n+1):
        multiple=[i*j for j in range(1,6)]
        multiple_list.append(multiple)
    return multiple_list
n=5
print(generate_multiples(n))