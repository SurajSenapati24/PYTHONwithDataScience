A = {10, 20, 30}
B = {5, 10, 15, 20}

# a) {30}
result_a = A - B
print("a) {30}: ", result_a)

# b) {5, 15, 30}
result_b = A ^ B
print("b) {5, 15, 30}: ", sorted(result_b))

# c) {5, 10, 15, 20, 30}
result_c = A | B
print("c) {5, 10, 15, 20, 30}: ", sorted(result_c))

# d) {10, 20}
result_d = A & B
print("d) {10, 20}: ", result_d)
