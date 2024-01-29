# Distinct Prime Factors https://projecteuler.net/problem=47

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

def primeFactorization(n):
    factors = []
    number = n
    while not isPrime(number):
       for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                number /= i
                factors.append(i)
                break
    factors.append(int(number))
    return factors

found = False
i = 6
factors = primeFactorization(2)
factors2 = primeFactorization(3)
factors3 = primeFactorization(4)
factors4 = primeFactorization(5)
while not found:
    i += 1
    factors = factors2
    factors2 = factors3
    factors3 = factors4
    factors4 = primeFactorization(i)
    if len(set(factors)) == 4 and len(set(factors2)) == 4 and len(set(factors3)) == 4 and len(set(factors4)) == 4:
        found = True
        print(i-3)

                
