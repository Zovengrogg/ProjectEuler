# Pandigital Multiples https://projecteuler.net/problem=38

maxPandigital = 0
for n in range(1, 100000):
    pandigits = '0'
    pandigital = True
    for j in range(1, 1000000):
        product = n*j
        for i in str(product):
            if i in pandigits:
                pandigital = False
                break
            pandigits += i
        if len(pandigits) == 10:
            break
    if pandigital:
        if int(pandigits) > maxPandigital:
            maxPandigital = int(pandigits)

print(maxPandigital)
