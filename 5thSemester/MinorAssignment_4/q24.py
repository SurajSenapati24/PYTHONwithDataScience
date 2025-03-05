def remove_tuples(lst,k):
    return [tup for tup in lst if len(tup)!=k]
l=[(1,2,3),(4,5,6),(1,),(0,2)]
l=remove_tuples(l,3)
print(l)