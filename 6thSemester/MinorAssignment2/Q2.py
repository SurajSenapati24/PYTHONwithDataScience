def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)
def main():
    x=int(input("Enter x: "))
    y=int(input("Enter y: "))
    print(f"GCD of {x} and {y} = {gcd(x,y)}")
if __name__=="__main__":
    main()