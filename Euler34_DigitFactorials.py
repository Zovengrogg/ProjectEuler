# Digit Factorials https://projecteuler.net/problem=34

from math import factorial

def factorialSum(n):
    sum = 0
    digits = [int(i) for i in str(n)]
    for digit in digits:
        sum += factorial(digit)
    return sum

total = 0
for n in range(3, 1000000):
    if n == factorialSum(n):
        total += n
    
print(total)

