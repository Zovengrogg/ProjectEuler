# Diophantine Equation https://projecteuler.net/problem=66

import time
from fractions import Fraction
from math import sqrt, floor, ceil

begin = time.time()

# x ** 2 - D * y ** 2 = 1
#   D = 13, x = 649, y = 180

def closestSquareRoot(number):
    return floor(sqrt(number))

def nextDigit(number, start, num, den):
    digit = 0
    trans = (number - (den * den))/num
    digit = floor((start + den)/trans)
    remainder = den - (trans * digit)
    return digit, trans, -remainder

def findContinuedFraction(number, start, length):
    continuedFraction = [start]
    digit, num, den = nextDigit(number, start, 1, start)
    continuedFraction.append(digit)
    limit = 1
    while limit < length:
        digit, num, den = nextDigit(number, start, num, den)
        continuedFraction.append(digit)
        limit += 1
    return continuedFraction

maxX = 0
d = 0
for i in range(2, 1001):
    a = floor(i ** .5)
    w = a * a
    if w != i:
        start = closestSquareRoot(i)
        x = 0
        iteration = 0
        while x == 0: 
            iteration += 1
            continuedFraction = findContinuedFraction(i, start, iteration)[::-1]
            den = continuedFraction[0]
            num = 1 + (continuedFraction[1] * den)
            continuedFraction = continuedFraction[2:]
            for digit in continuedFraction:
                prevDen = den
                den = num
                num = prevDen + (digit * den)
            if num ** 2 - i * den ** 2 == 1:
                x = num
        if x > maxX:
            maxX = x   
            d = i

print(d)


print("My program took", time.time() - begin, "to run.")