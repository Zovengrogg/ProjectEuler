# Pandigital Prime https://projecteuler.net/problem=41

from math import sqrt
from itertools import permutations

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

# def isPandigital(n):
#     pandigits = [0]
#     for digit in n:
#         if digit in pandigits:
#             return False
#         pandigits.append(digit)
#     return True

def findPanPrime(panLen):
    for n in reversed(panLen):
        pandigitals = permutations(reversed(range(1, n+1)))
        for num in pandigitals:
            number = 0
            for digit in num:
                number *= 10
                number += digit
            if isPrime(number):
                return number
        
print(findPanPrime(range(1,10)))