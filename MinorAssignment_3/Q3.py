def evenSquares():
    sum=0
    for i in range(0,51,2):
            i*=i
            sum+=i
    return sum
print(evenSquares())