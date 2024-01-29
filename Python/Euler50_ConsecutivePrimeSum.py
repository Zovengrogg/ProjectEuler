# Consecutive Prime Sum https://projecteuler.net/problem=50

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

summation = 2
prime = 3
primes = [2]
while prime < 500000:
    if isPrime(prime):
        primes.append(prime)
        summation += prime
    prime += 2

found = False
beg = 0
end = 21
length = 20
while not found:
    primeSum = 0
    start = beg
    stop = end
    while primeSum < 1000000:
        primeSum = sum(primes[i] for i in range(start, stop))
        if isPrime(primeSum):
            if length < stop - start:
                length = stop - start
                print(primeSum, length)
                break
        start += 1
        stop += 1
    end += 1
    if sum(primes[i] for i in range(beg, end)) > 1000000:
        found = True