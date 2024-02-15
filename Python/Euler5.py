# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

# Multiply the primes not including 2 and 5 because we are including 20
thing = 3 * 7 * 11 * 13 * 17 * 19 * 20
i = 1
while True:
    num = thing * i
    if (num % 16 == 0) & (num % 18 == 0) & (num % 15 == 0) & (num % 14 == 0) & (num % 12 == 0):
        break
    i += 1
print(num)
