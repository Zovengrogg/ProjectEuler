# Powerful Digit Sum https://projecteuler.net/problem=56

import time
# import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()

print(max([sum([int(digit) for digit in str(a**b)]) for a in range(100) for b in range(100)]))

print("My program took", time.time() - start, "to run.")