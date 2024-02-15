from math import sqrt


# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


i = 0
x = 1
while i < 10001:
    x += 1
    if is_prime(x):
        i += 1
print(x)
