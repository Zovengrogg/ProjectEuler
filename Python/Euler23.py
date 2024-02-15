# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import sqrt
import time

start = time.time()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
          151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
          199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
          263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
          317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
          383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
          443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
          503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
          577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
          641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
          701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
          769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
          839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
          911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
          983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033]


def aliquot_sum(n):
    i = 0
    num = n
    ali_sum = 1
    while primes[i] <= sqrt(num):
        p = primes[i]
        a = 1
        while num % p == 0:
            num /= p
            a += 1
        ali_sum = ali_sum * (p ** a - 1) / (p - 1)
        i += 1
    if num != 1:
        ali_sum = ali_sum * (num + 1)
    ali_sum -= n
    return ali_sum


abundant = []
deficient = []
for n in range(2, 28123):
    if aliquot_sum(n) > n:
        abundant.append(n)
for n in range(2, 28123):
    if aliquot_sum(n) < n:
        deficient.append(n)


end = time.time()
print(end - start)
