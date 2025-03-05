def print_ap_terms(f_term, diff):
    terms = []
    for i in range(10):
        term = f_term + i * diff
        terms.append(term)
    print("The first 10 terms of the arithmetic progression are:", terms)

f_term = int(input("Enter the first term of the AP: "))
diff = int(input("Enter the common difference of the AP: "))
print_ap_terms(f_term, diff)
