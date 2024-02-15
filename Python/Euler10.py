# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def lowsum(n):
    i = 3
    sum = 2
    while i < n:
        if is_prime(i):
            sum += i
        i += 2
    return sum


print(lowsum(2000000))
