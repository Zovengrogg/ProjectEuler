# Prime Digit Replacement https://projecteuler.net/problem=51

import time
from math import sqrt
from itertools import *

# The replacable digit cannot be the last digit (It would not be prime 5/10 times)
# Ones place must be 1, 3, 7 or 9 otherwise it will not be prime
# The number of digits that are replaced must be a multiple of 3 AND the startic digits must not add up to a multiple of 3
    # The reason for the above rule is that if the startic digits add up to something that is divided by 3 then the number will be divided by three every time along with above rule.
    # If we change digits by a number that is not divisible by three then once in every three increments the number will be divisible by
    # three and thus at least 3 out of the ten generated numbers will not be prime. 


# start = time.time()

# def isPrime(n):
#     if n > 1:
#         for i in range(2, int(sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     return False

# def primes(n):
#     s = list(range(3, n+1, 2))
#     mroot = n ** 0.5
#     half = (n+1)//2-1
#     i=0
#     m=3
#     while m <= mroot:
#         if s[i]:
#             j = (m*m-3)//2
#             s[j] = 0
#             while j < half:
#                 s[j] = 0
#                 j += m
#         i = i + 1
#         m = 2*i + 3
#     return [2]+[x for x in s if x]
    
# digits = []
# found = False
# numOfStaticDigits = 0
# numOfVarDigits = 3 

# while not found:      
#     wrong = 0
#     for x in range(0, 10):
#         lastDigit = 1 
#         comb = permutations([1, 2, 3], 3)
#         if not isPrime(int(number)):
#             wrong += 1
#         if wrong == 2:
#             break
#     if wrong != 2:
#         found = True
#         break 

#     for x in range(0, 10):
#         lastDigit = '3'
#         number = str(x)+str(x)+str(x)+lastDigit
#         if not isPrime(int(number)):
#             wrong += 1
#         if wrong == 3:
#             break
#     if wrong < 3:
#         found = True
#         break 

#     for x in range(0, 10):
#         lastDigit = '7'
#         number = str(x)+str(x)+str(x)+lastDigit
#         if not isPrime(number):
#             wrong += 1
#         if wrong == 2:
#             break
#     if wrong != 2:
#         found = True
#         break 

#     for x in range(0, 10):
#         lastDigit = '9'
#         number = str(x)+str(x)+str(x)+lastDigit
#         if not isPrime(number):
#             wrong += 1
#         if wrong == 2:
#             break
#     if wrong != 2:
#         found = True
#         break 



# print("My program took", time.time() - start, "to run.")

start = time.time()
def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

# Generate all 6-digit prime numbers
primes = {int(str(i) + j + k + l + m + n)
          for i in '123456789'
          for j in '0123456789'
          for k in '0123456789'
          for l in '0123456789'
          for m in '0123456789'
          for n in '1379'  # last digit can't be even or 5
          if isPrime(int(str(i) + j + k + l + m + n))}

# Find 6-digit primes that can form an 8-prime value family
for prime in primes:
    for num_replaced in [3, 6]:  # only consider replacing 3 or 6 digits
        for digits in combinations('1234679', num_replaced):
            family = []
            for digit in '0123456789':
                num = str(prime)
                for d in digits:
                    num = num.replace(d, digit)
                if num[0] != '0' and int(num) in primes:
                    family.append(int(num))
            if len(family) == 8:
                print(min(family))
                print("My program took", time.time() - start, "to run.")
                exit()
