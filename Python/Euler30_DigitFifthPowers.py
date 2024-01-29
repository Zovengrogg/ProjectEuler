# Digit Fifth Powers https://projecteuler.net/problem=30
def sumOfFifthPower(n):
    digits = [int(i) for i in str(n)]
    result = 0
    for j in digits:
        result = result + j**5
    return result

digitFifthPowers = []
for n in range(2, 1000000):
    if(n == sumOfFifthPower(n)):
        digitFifthPowers.append(n)
        print(digitFifthPowers)

sum = 0
for x in digitFifthPowers:
    sum += x

print(sum)