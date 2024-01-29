# Permuted Multiples https://projecteuler.net/problem=52

import time
import collections

# x 2x 3x 4x 5x 6x all share the same digits

# Rule: z//6 > x > z/10 here z = 10^y and y is the number of digits of x
# 

# 1 will create 1,2,3,4,5,6
# 2 will create 2,4,6,8,10,12
# 3 will create 3,6,9,12,15,18
# 4 will create 4,8,12,16,20,24
# 5 will create 5,10,15,20,25,30
# 6 will create 6,12,18,24,30,36
# 7 will create 7,14,21,28,35,42
# 8 will create 8,16,24,32,40,48
# 9 will create 9,18,27,36,45,54

# Think programatically...
# Other rules?
# Let's do a brute force first

start = time.time()

x=125874
if collections.Counter([digit for digit in str(2*x)]) == collections.Counter([digit for digit in str(2*x)]):
    print(2*x)


answer = 0
x = 100
y = 3
while answer == 0:
    if x > 10**y//6:
        x = 10**(y)
        y += 1
        continue

    digits = [digit for digit in str(x)]

    if collections.Counter(digits) != collections.Counter([digit for digit in str(2*x)]):
        x += 1
        continue
    
    if collections.Counter(digits) != collections.Counter([digit for digit in str(3*x)]):
        x += 1
        continue

    if collections.Counter(digits) != collections.Counter([digit for digit in str(4*x)]):
        x += 1
        continue
    
    if collections.Counter(digits) != collections.Counter([digit for digit in str(5*x)]):
        x += 1
        continue

    if collections.Counter(digits) != collections.Counter([digit for digit in str(6*x)]):
        x += 1
        continue

    answer = x
    print(answer)

print("My program took", time.time() - start, "to run.")

# A short and simple answer found on forums.
i = 1
while len({frozenset(str(i*x)) for x in range(1, 7)}) > 1:
    i += 1
print(i)