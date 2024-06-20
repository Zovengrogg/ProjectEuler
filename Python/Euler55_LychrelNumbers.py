# Lychrel Numbers https://projecteuler.net/problem=55

import time
# import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()
print("Start")

def IsPalindrome(n):
    return str(n) == str(n)[::-1]

numbers = [i for i in range(1, 10000)]
lychrel = 0
while len(numbers) > 0:
    temp = numbers[0]
    check = numbers[0]
    tempNumbers = []
    for j in range(51):
        tempNumbers.append(temp)
        tempNumbers.append(int(str(temp)[::-1]))
        temp += int(str(temp)[::-1])
        if IsPalindrome(temp):
            for i in tempNumbers:
                if i in numbers:
                    numbers.remove(i)
            break
    if check == numbers[0]:
        lychrel += 1
        numbers.remove(check)

print(lychrel)
print("My program took", time.time() - start, "to run.")