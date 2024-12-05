"""Write a program to enter names and percentage of marks in a dictionary and display the information
 on the screen."""
dic={}
n=int(input("How many data do you want in dictionary: "))
for _ in range(n):
    name=input("Enter name: ")
    per=int(input("Enter percentage of marks: "))
    dic[name]=per
print("Name\t\tPercentage")
for key,val in dic.items():
    print(f"{key}\t{val}%")