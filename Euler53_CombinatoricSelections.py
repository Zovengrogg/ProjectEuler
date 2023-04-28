# Combinatoric Selections https://projecteuler.net/problem=53

import time
from math import factorial as f
from itertools import *

start = time.time()

# I think this can be brute forced. Start at n = 100 then check if the combinations are greater than
# a million. Start with n // 2 for r then work down and up until it is less than a million. 
# Move on to n = 99 etc

def comb(n, r):
    return f(n)/(f(r)*f(n-r))

total = 0
for n in range (2, 101, 2):
    r = n//2

    if comb(n, r+1) > 1000000:
        total += 1
        r -= 1

    while comb(n, r) > 1000000:
        total += 2
        r -= 1

for n in range(1, 100, 2):
    r = n//2

    while comb(n, r) > 1000000:
        total += 2
        r -= 1

print(total)
print("My program took", time.time() - start, "to run.")