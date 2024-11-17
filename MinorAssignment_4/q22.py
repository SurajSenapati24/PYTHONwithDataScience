l=[10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
l1=list(map(lambda x:x*2,filter(lambda x:x%2==0,l)))
l2=list(filter(lambda x:x%2==0,map(lambda x:x*2,l)))
print(l1)
print(l2)