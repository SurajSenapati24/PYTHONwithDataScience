def print_increasing_numbers(n, current_number="", last_digit=0):
    if len(current_number) == n:
        print(current_number, end=" ")
        return
    for digit in range(last_digit + 1, 10):
        print_increasing_numbers(n, current_number + str(digit), digit)
n = 2
print_increasing_numbers(n)