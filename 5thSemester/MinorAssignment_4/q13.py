def sorted_tuple(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])
tuples_list = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_list = sorted_tuple(tuples_list)
print("Original List:", tuples_list)
print("Sorted List:", sorted_list)