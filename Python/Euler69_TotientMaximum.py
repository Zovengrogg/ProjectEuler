# Totient Maximum https://projecteuler.net/problem=69

import time
from math import sqrt

start = time.time()


def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


i = 6
x = 3
while i < 1000000:
    x += 2
    if is_prime(x):
        i *= x
i = i/x
print(i)


print("My program took", time.time() - start, "to run.")