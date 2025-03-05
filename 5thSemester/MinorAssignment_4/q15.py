import random

def gen_matrix(r, c):
    return [[random.randint(0, 1) for _ in range(c)] for _ in range(r)]

def max_row(m):
    return [sum(r) for r in m].index(max([sum(r) for r in m]))

def max_col(m):
    return max(range(len(m[0])), key=lambda c: sum(row[c] for row in m))

m = gen_matrix(4, 4)

for r in m:
    print("".join(map(str, r)))

print(f"The largest row index: {max_row(m)}")
print(f"The largest column index: {max_col(m)}")
