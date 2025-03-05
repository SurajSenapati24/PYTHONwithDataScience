def analyze(list1, list2):
    set1, set2 = set(list1), set(list2)
    sym_diff = set1 ^ set2
    result = []
    
    for num in sym_diff:
        if num % 2 == 0:
            result.append(num * 2)
        else:
            result.append(num + 5)
    
    return sorted(result)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(analyze(list1, list2))
