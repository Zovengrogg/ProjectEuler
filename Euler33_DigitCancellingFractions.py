# Digit Cancelling Fractions https://projecteuler.net/problem=33

from fractions import Fraction

def canDoStupidMath(numerator, denominator):
    value = numerator/denominator
    stupidValue = 0
    num = [int(i) for i in str(numerator)]
    den = [int(i) for i in str(denominator)]
    for i in num: 
        if i in den:
            den.remove(i)
            num.remove(i)
            stupidValue = num[0]/den[0]
    if stupidValue == value:
        return True
    return False

answers = []
for n in range(11, 99):
    for d in range(11, 99):
        if n >= d or '0' in str(n) or '0' in str(d):
            continue
        if canDoStupidMath(n, d):
            answers.append([n,d])

numAns = 1
denAns = 1
for fractions in answers:
    numAns *= fractions[0]
    denAns *= fractions[1]
print(Fraction(numAns, denAns))
        
    