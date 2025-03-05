"""Write a program to take a user-input dictionary and print the sum of the values."""
nums={}
n=int(input("How many numbers do you want in the dictionary: "))
for i in range(n):
    num=int(input("Enter number: "))
    nums[i]=num
s=sum(nums.values())
print("The sum is: ",s)