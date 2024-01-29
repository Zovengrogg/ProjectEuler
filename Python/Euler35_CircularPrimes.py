# Circular Primes https://projecteuler.net/problem=35

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

answers = []
for n in range(2, 1000000):
    digits = [i for i in str(n)]
    circular = True
    for index in range(0, len(digits)):
        newPrime = ''
        for g in range(0, len(digits)):
            newPrime += digits[(index+g)%len(digits)]
        if not isPrime(int(newPrime)):
            circular = False
            break
    if circular:
        answers.append(n)

print(len(answers), answers)