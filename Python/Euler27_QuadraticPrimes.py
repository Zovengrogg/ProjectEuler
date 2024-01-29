# Quadratic Primes https://projecteuler.net/problem=27

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def quadraticPrimeLength(a, b):
    n = 0
    prime = True
    while(prime):
        prime = isPrime(n*n+a*n+b)
        n += 1
    return n

lengthAB = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if(quadraticPrimeLength(a,b) > lengthAB[0]):
            lengthAB = quadraticPrimeLength(a,b), a, b
print(lengthAB)