def find_greatest_digits(num):
    num_str = str(num)
    digits = [int(char) for char in num_str]
    unique = list(set(digits))
    unique.sort(reverse=True)
    first = unique[0] if len(unique) > 0 else None
    second = unique[1] if len(unique) > 1 else None
    third = unique[2] if len(unique) > 2 else None
    print(f"{first},{second},{third}")  

num = 123
find_greatest_digits(num)
