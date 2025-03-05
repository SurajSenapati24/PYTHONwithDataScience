"""Write a function that takes a number as an input parameter and returns the corresponding text in
 words, e.g., on input 452, the function should return ‘Four Five Two’. Use a dictionary for mapping
 digits to their string representation."""
def number_to_words(n):
    dtow = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    n_str = str(n)
    words = [dtow[int(digit)] for digit in n_str]
    return ' '.join(words)
n=int(input("Enter a number: "))
result = number_to_words(n)
print(f"The number {n} in words is: '{result}'")
