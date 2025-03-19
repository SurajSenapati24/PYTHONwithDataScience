import random
def quickselect(a, k):
    def select(l, r, k):
        if l == r:
            return a[l]
        p = random.randint(l, r)
        p = partition(l, r, p)
        if k == p:
            return a[p]
        elif k < p:
            return select(l, p - 1, k)
        else:
            return select(p + 1, r, k)

    def partition(l, r, p):
        v = a[p]
        a[p], a[r] = a[r], a[p]
        s = l
        for i in range(l, r):
            if a[i] > v:
                a[i], a[s] = a[s], a[i]
                s += 1
        a[r], a[s] = a[s], a[r]
        return s

    k = len(a) - k
    return select(0, len(a) - 1, k)

arr = [3, 2, 1, 5, 6, 4]
k = 2
print(quickselect(arr, k))