# Triangular, Pentagonal, and Hexagonal https://projecteuler.net/problem=45

from math import sqrt

def isPentagonal(n):
    number = (sqrt(24*n + 1) + 1)/6
    if number.is_integer():
        return True
    return False

def isTriangular(n):
    number = (sqrt(8*n + 1) + 1)/2
    if number.is_integer():
        return True
    return False

found = False
i = 143
while not found:
    i += 1
    hexagonal = 2*i*i-i
    if isPentagonal(hexagonal) and isTriangular(hexagonal):
        found = True
        print(hexagonal)

