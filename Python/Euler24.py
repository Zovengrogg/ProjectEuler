# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1,
# 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

decrement = lambda digit: digit - 1

mod = lambda term, digit: (term - (term % math.factorial(digit))) / math.factorial(digit)

remainder = lambda term, digit: term - mod(term, decrement(digit)) * math.factorial(decrement(digit))


def solve(term, digit):
    temp = term-1
    for x in range(digit, 0, -1):
        print(mod(temp, decrement(x)))
        temp = remainder(temp, x)
    # results = [remainder(temp, x) for x in range(digit, 0, -1)]
    # print(results)


solve(1000000, 10)



# 2783915460