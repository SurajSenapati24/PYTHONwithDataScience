def print_ap_terms(f_term, difference):
    terms = []
    for i in range(10):
        term = f_term + i * difference
        terms.append(term)
    print("The first 10 terms of the arithmetic progression are:", terms)

f_term = int(input("Enter the first term of the AP: "))
difference = int(input("Enter the common difference of the AP: "))
print_ap_terms(f_term, difference)
