# Prime Pair Set https://projecteuler.net/problem=65

import time
from fractions import Fraction
from math import sqrt, floor, ceil

start = time.time()

def sequence_of_e(number):
    e = [2]
    for k in range(1, (number + 2)//3):
        e.append(1)
        e.append(2*k)
        e.append(1)
    if (number - 1) % 3 == 1:
        e.append(1)
    if (number - 1) % 3 == 2:
        e.append(1)
        e.append(2*((number + 2) //3))
    return e

def getSum(n): 
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
        
e = sequence_of_e(100)[::-1]
den = e[0]
num = 1 + (e[1] * den)
e = e[2:]
for x in e:
    prevDen = den
    den = num
    num = prevDen + (x * den)


fraction = Fraction(num, den)

print(getSum(fraction.numerator))


print("My program took", time.time() - start, "to run.")