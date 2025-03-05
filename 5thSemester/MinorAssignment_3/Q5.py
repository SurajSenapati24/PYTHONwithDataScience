#Write a function that takes a positive integer and returns the number of digits.
def count_digits(num):
    count=0
    while num>0:
        num//=10
        count+=1
    return count
def count_digitss(num):
    numstr=str(num)
    return len(numstr)
num=int(input("Enter a number: "))
print(count_digitss(num))
print(count_digits(num))