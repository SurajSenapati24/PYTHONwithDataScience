def number_to_words(num):
    map = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    if num == 0:
        return map[0]
    s = ""
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)  
        num //= 10
    digits.reverse()
    for digit in digits:
        s += map[digit] + " "
    return s.strip() 

user = int(input("Enter a number: "))
print(f"The number in words is: {number_to_words(user)}")
