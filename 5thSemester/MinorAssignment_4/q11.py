'''Write a Python program to print M-by-N list in the tabular format.'''
l=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for row in l:
    for i in row:
        print(f"{i:<4}",end='')
    print()