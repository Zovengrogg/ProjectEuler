# Prime Pair Set https://projecteuler.net/problem=64

import time
from math import sqrt, floor, ceil

start = time.time()

def closestSquareRoot(number):
    return floor(sqrt(number))

# sqrt(3) -> 1/(sqrt(3) - 1) = 1*(sqrt(3) + 1)/2 = (sqrt(3) + 1)/(2/1) = 1 + (sqrt(3) - 1)/2
#                                                                                          ->trans

def nextDigit(number, start, num, den):
    digit = 0
    trans = (number - (den * den))/num
    digit = floor((start + den)/trans)
    remainder = den - (trans * digit)
    return digit, trans, -remainder

def findPeriod(number, start):
    period = []
    digit, num, den = nextDigit(number, start, 1, start)
    period.append(digit)
    while num != 1 or den != start:
        digit, num, den = nextDigit(number, start, num, den)
        period.append(digit)
    return len(period)

odd = []
for x in range(2, 10001):
    y = floor(x ** .5)
    w = y * y
    if w != x:
        start = closestSquareRoot(x)
        if(findPeriod(x, start) % 2 == 1):
            odd.append(x)

print(len(odd))


print("My program took", time.time() - start, "to run.")