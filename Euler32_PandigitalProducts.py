# Pandigital Products https://projecteuler.net/problem=32

from math import sqrt

def factor(n):
    factors = []
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            factors.append([i, int(n/i)])
    return factors

def checkFactors(factors, digits):
    # Not sure why I can't set this to digits
    digitList = [i for i in digits]
    for factor in factors:
        for i in str(factor):
            if(int(i) in digitList):
                return False
            digitList.append(int(i))
    if(len(digitList) == 10):
        return True
    return False

answers = []
for n in range(1234, 9876):
    panDigital = True
    digits = [0]
    for i in str(n):
        if(int(i) in digits):
            panDigital = False
            break
        digits.append(int(i))
    if panDigital == False:
        continue
    factors = factor(n)
    for pairs in factors:
        if(checkFactors(pairs, digits)):
            answers.append(n)
            break

sum = 0
for a in answers:
    sum += a
print(sum)
    

    