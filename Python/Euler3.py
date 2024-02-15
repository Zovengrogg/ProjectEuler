# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 
# 600851475143 ?

#User input
number = input("What number do you want to check the largest prime factorization of? ")
number = int(number)

from math import sqrt

primes = set([2])
value = 3
number = 600851475143
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print(value)
            number /= value
print(number)
