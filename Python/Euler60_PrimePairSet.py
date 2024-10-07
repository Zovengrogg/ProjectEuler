# Prime Pair Set https://projecteuler.net/problem=60

import time
import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()

def IsPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def IsPrimePair(a, b):
    return IsPrime(int(str(a)+str(b))) and IsPrime(int(str(b)+str(a)))

def PrimePairSet(n):
    primes = [i for i in range(3, n, 2) if IsPrime(i)]
    for a in primes:
        for b in primes:
            if a < b:
                if IsPrimePair(a, b):
                    for c in primes:
                        if c > b:
                            if IsPrimePair(a, c) and IsPrimePair(b, c):
                                for d in primes:
                                    if d > c:
                                        if IsPrimePair(a, d) and IsPrimePair(b, d) and IsPrimePair(c, d):
                                            for e in primes:
                                                if e > d:
                                                    if IsPrimePair(a, e) and IsPrimePair(b, e) and IsPrimePair(c, e) and IsPrimePair(d, e):
                                                        return [a, b, c, d, e]
primePairSet = PrimePairSet(10000)
print(primePairSet)
print(sum(primePairSet))

print("My program took", time.time() - start, "to run.")