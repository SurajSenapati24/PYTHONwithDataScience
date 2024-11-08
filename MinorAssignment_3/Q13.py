def roman_to_integer(roman):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_v = 0
    for char in reversed(roman):
        curr_v = romans[char]
        if curr_v < prev_v:
            total -= curr_v
        else:
            total += curr_v
        prev_v = curr_v
    return total

print(roman_to_integer("LVIII"))

