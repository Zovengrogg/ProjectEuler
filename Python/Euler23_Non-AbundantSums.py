# Non-abundant Sums https://projecteuler.net/problem=23

import time
from math import sqrt

start_time = time.time()

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

def factorization(n):
    factors = [1]
    if not isPrime(n):
       for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if n/i != i:
                    factors.append(int(n/i))
    return factors


def isAbundant(n):
    return sum(factorization(n)) > n

abundants = []
for n in range(12, 20162):
    if isAbundant(n):
        abundants.append(n)

# First try

notSumOfAbundant = 0
for m in range(1, 49):
    sumOfAbundant = False
    for abundant in abundants:
        if abundant > m/2:
            break
        if m - abundant in abundants:
            sumOfAbundant = True
            break
    if not sumOfAbundant:
        notSumOfAbundant += m
for m in range(49, 20162, 2):
    sumOfAbundant = False
    for abundant in abundants:
        if abundant > m/2:
            break
        if m - abundant in abundants:
            sumOfAbundant = True
            break
    if not sumOfAbundant:
        notSumOfAbundant += m

print(notSumOfAbundant)
print("My program took", time.time() - start_time, "to run")

# Short but long running

# def abundantsum(i):
#         return any(i-a in abundants for a in abundants)

# print(sum(i for i in range(1,28124) if not abundantsum(i)))

# Second try for faster time (NOPE)

# abundantSums = []
# for abundant in abundants:
#     for abundant2 in abundants:
#         if abundant + abundant2 > 20162:
#             break
#         abundantSums.append(abundant + abundant2)
# sum(i for i in range(1,20162) if i not in abundantSums)
        
# print("My program took", time.time() - start_time, "to run")