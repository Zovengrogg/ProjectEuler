# Sub-String Divisibility https://projecteuler.net/problem=43

from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]
def substringsPrimeDivisible(listOfDigits):
    d = [str(i) for i in listOfDigits]
    
    for j in range(7):
        if int(d[j+1]+d[j+2]+d[j+3])%primes[j] != 0:
            return False 
    return True

sum = 0
pandigitals = permutations(range(0, 10))
for n in pandigitals:
    if substringsPrimeDivisible(n):
        sum += int(''.join(map(str,n)))

print(sum)
