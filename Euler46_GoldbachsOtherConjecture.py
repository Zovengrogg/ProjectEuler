# Goldbach's Other Conjecture https://projecteuler.net/problem=46

from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

found = False
n = 33
while not found:
    n += 2
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            squares = []
            square = 1
            exactSum = False
            while not exactSum:
                if 2*square*square > n:
                    break
                squares.append(2*square*square)
                square += 1
            for doubleSquare in squares:
                if isPrime(n - doubleSquare):
                    exactSum = True
                    break
            if not exactSum:
                found = True
                print(n)
            break


                

