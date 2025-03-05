'''Write a Python program that removes all occurrences of a specific element from a list.'''
l=[1,2,3,1,4,5,1,7]
occurence=int(input("Enter the element to remove all the occurences"))
for i in l:
    if(i==occurence):
        l.remove(i)
print(l)