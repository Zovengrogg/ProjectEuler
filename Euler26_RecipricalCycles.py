# Reciprical Cycles https://projecteuler.net/problem=26



def cycleLength(n):
    numerator = 10
    length = []
    while(n > numerator):
        numerator *= 10
    qutient, remainder = divmod(numerator, n)
    first = remainder
    length.append(remainder)
    while(n > remainder and remainder != 0):
        remainder *= 10
    qutient, remainder = divmod(remainder, n)
    while(not remainder in length and remainder != 0):
        length.append(remainder)
        while(n > remainder):
            remainder *= 10
        qutient, remainder = divmod(remainder, n)
    return len(length)

maxLen = 0
for x in range(2, 1000):
    length = cycleLength(x)
    if(length > maxLen):
        maxLen = length
        print(x, maxLen)