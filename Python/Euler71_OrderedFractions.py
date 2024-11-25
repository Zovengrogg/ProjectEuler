# Ordered Fractions https://projecteuler.net/problem=71

import time
from math import gcd

def solution():
    left_of = 0
    n = 0
    d = 0
    for x in range(999999, 2, -1):
        for y in range(x-1, 1, -1):
            if(left_of < y/x < 3/7):
                if(gcd(y, x) == 1):
                    left_of = y/x
                    n = y
                    d = x
                    return n, d

n, d = solution()          
print(n, d)
            