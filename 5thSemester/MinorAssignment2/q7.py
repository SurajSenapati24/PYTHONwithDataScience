def isprime(n):
    if n <= 1:  # 1 and below are not prime numbers
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    s = 0
    for i in range(2, n + 1):  # Primes start from 2
        if isprime(i):
            s += i
    return s

s = sum_primes(20)
print(s)
