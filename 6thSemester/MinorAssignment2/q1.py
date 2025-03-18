def power(base,exponent):
    if exponent==1:
        return base
    return base*power(base,exponent-1)
def main():
    base=int(input("Enter base: "))
    exp=int(input("Enter exponent: "))
    print(f"{base} to the power {exp} = {power(base,exp)}")
if __name__=="__main__":
    main()