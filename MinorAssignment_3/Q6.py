#Define a function to check if a given string is a palindrome. Example: madam ⟲ madam, racecar ⟲ racecar.
def palindrome(s):
    n=s[::-1]
    if s==n:
        return True
    else:
        False
user=input("Enter a String: ")
print("Is Palindrome: ",palindrome(user))