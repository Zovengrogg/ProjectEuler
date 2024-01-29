# Prime Permutations https://projecteuler.net/problem=49

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

for i in range(1000, 5000):
    for j in range(1000, 10000-2*i):
        if isPrime(j) and isPrime(j+i) and isPrime(j+2*i):
            digits1 = [int(d) for d in str(j)]
            digits2 = [int(d) for d in str(j+i)]
            digits3 = [int(d) for d in str(j+2*i)]
            digits1.sort()
            digits2.sort()
            digits3.sort()
            if digits1 == digits2 == digits3:
                print(str(j)+str(j+i)+str(j+2*i))