def find_greatest_digits(number):
    num_str = str(number)
    digits = [int(char) for char in num_str]
    unique_digits = list(set(digits))
    unique_digits.sort(reverse=True)
    first = unique_digits[0] if len(unique_digits) > 0 else None
    second = unique_digits[1] if len(unique_digits) > 1 else None
    third = unique_digits[2] if len(unique_digits) > 2 else None
    print(f"{first} {second} {third}")

number = 123
find_greatest_digits(number)
