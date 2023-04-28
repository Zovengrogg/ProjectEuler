# Truncatable Primes https://projecteuler.net/problem=37

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

answers = []
for n in range(11, 1000001, 2):
    if not isPrime(n):
        continue
    digits = str(n)
    truncatable = True
    newPrimeRight = digits
    newPrimeLeft = digits
    for index in range(1, len(digits)):
        newPrimeRight = newPrimeRight[1:]
        newPrimeLeft = newPrimeLeft[:-1]
        if not isPrime(int(newPrimeRight)) or not isPrime(int(newPrimeLeft)):
            truncatable = False
            break
    if truncatable:
        answers.append(n)

total = 0
for a in answers:
    total += a
print(total)