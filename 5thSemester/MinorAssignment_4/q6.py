"""Input 10 integers from the keyboard into a list. The number to be searched is entered through the
 keyboard by the user. Write a Python program to find if the number to be searched is present in the
 list and if it is present, display the number of times it appears in the list."""
l=[]
for i in range(10):
    user=int(input("Enter a number: "))
    l.append(user)
search=int(input("Enter a number to search: "))
if search in l:
    print(f"Number of times {search} is present in the list is: {l.count(search)}")
else:
    print("Not preset in the list")