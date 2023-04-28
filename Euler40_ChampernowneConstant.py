# Champernowne's Constant https://projecteuler.net/problem=40

def position(n):
    index = 0

    champConst = ''
    while len(champConst) != n:
        index += 1
        for i in str(index):
            champConst += i
            if len(champConst) == n:
                return int(i)

answer = position(1)*position(10)*position(100)*position(1000)*position(10000)*position(100000)*position(1000000)
print(answer)


# ChatGPT
fraction = ""
n = 1

# Build the fraction by concatenating positive integers
while len(fraction) < 1000000:
    fraction += str(n)
    n += 1

# Compute the product of the specified digits
product = 1
for i in range(7):
    digit = int(fraction[10**i - 1])
    product *= digit

print(product)