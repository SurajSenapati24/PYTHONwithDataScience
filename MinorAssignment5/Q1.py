"""Write a program to accept student name and marks from the user and create a dictionary. Also, display
 student marks by taking student name as input."""
students={}
n=int(input("How many student's name and marks you want to enter: "))
for _ in range(n):
    name=input("Enter name: ")
    mark=int(input("Enter marks: "))
    students[name]=mark
search = input("\nEnter the name of the student to display marks: ")
if search in students:
    print(f"{search}'s marks: {students[search]}")
else:
    print(f"Student named {search} not found.")
