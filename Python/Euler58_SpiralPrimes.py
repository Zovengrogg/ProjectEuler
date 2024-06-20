# Spiral Primes https://projecteuler.net/problem=58

import time
# import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()



def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

sideLength = 3
primes = 3
diagonal = [1, 3, 5, 7, 9]
while primes/len(diagonal) > 0.1:
    sideLength += 2
    newDiagonal = [sideLength**2 - i*(sideLength-1) for i in range(4)]
    diagonal += newDiagonal
    primes += sum([isPrime(i) for i in newDiagonal])

print(sideLength)

print("My program took", time.time() - start, "to run.")