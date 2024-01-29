# Pentagon Numbers https://projecteuler.net/problem=44

from math import sqrt
# We want values for j and k such that:
    # (3j^2-j+3k^2-k)/2 = 3m^2-m and
    # (3j^2-j-3k^2-k)/2 = 3n^2-n
    # Where j > k and D = 3n^2-n is minimized

# Possible starting points:
    # Brute Force - combinations of j and k within a certain range
    # Brute Force - start with 3n^2-n 
    # Brute Force - Create is pentagon method

def isPentagonal(n):
    number = (sqrt(24*n + 1) + 1)/6
    if number.is_integer():
        return True
    return False

found = False
i = 1
while not found:
    i += 1
    n = i*(3*i-1)/2

    for j in reversed(range(1, i)):
        m = j*(3*j-1)/2
        if isPentagonal(n - m) and isPentagonal(n + m):
            print(n-m)
            found = True
            break
            




    