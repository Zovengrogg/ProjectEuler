# The sum of the squares of the first ten natural numbers is,
# 1 + 4 + 25 + ... + 100 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of
# the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.

sumOfSquares = 0
squareOfSums = 0
for x in range(101):
    sumOfSquares += x * x
for x in range(101):
    squareOfSums += x
squareOfSums = squareOfSums * squareOfSums
difference = squareOfSums - sumOfSquares
print(difference)
