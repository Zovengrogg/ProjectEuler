# Square Root Convergents https://projecteuler.net/problem=57

import time
# import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()

higherNum = 0
currentNum = 3
previousNum = 1
currentDen = 2
previousDen = 1
for i in range(2, 1000):
    num = currentNum + 2*currentDen
    den = currentNum + currentDen
    previousNum = currentNum
    currentNum = num
    previousDen = currentDen
    currentDen = den
    if len(str(currentNum)) > len(str(currentDen)):
        higherNum += 1

print(higherNum)

print("My program took", time.time() - start, "to run.")