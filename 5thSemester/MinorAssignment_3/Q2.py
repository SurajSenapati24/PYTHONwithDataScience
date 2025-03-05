def function():
    l=[]
    for i in range(101,500):
        if(i%3==0 and i%5==0):
            l.append(i)
    return l
print(function())
