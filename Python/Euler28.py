# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time
from functools import reduce
from operator import mul

start = time.time()

square = lambda x: x ** 2
add = lambda x: 4 * square(x) - 6 * (x - 1)


def solve(y):
    # sum = [add(length) for length in range(3, y + 1, 2)]
    # result = reduce(lambda x, y: x+y, sum) + 1
    # print(result)

    # 0.48919224739074707

    sum = 0
    for length in range(3, y + 1, 2):
        sum += add(length)
    sum += 1
    print(sum)


# 0.3904697895050049

solve(1000001)

print(time.time() - start)
