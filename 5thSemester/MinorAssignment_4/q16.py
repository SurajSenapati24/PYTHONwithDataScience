def is_sorted(lst):
    return lst == sorted(lst)
user_input = input("Enter list: ")
lst = list(map(int, user_input.split()))
if is_sorted(lst):
    print("The list is already sorted.")
else:
    print("The list is not sorted.")
