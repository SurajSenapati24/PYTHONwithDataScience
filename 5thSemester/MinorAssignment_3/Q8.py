#Write a Python program that takes the name of a month as input and returns the number of days in
# that month.
# Input: The name of the Month: February
# Output: No. of days: 28/29 days
def daysInMonth(month):
    month.lower()
    if(month=="february"):
        return "28/29"
    elif(month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december"):
        return "31"
    elif(month=="april" or month=="june" or month=="september" or month=="november"):
        return "30"
    else:
        return "Invalid Input"
user=input("The name of the Month: ")
print(f"No. of days: {daysInMonth(user)}")
