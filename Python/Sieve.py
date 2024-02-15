from math import sqrt
import time

# Used to find primes. The is_prime function is the sieve of Eratosthenes

for x in range(10):
    start = time.time()
    def is_prime(n):
        if n <= 1:
            return False
        for x in range(2, int(sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True


    def lowsum(n):
        i = 3
        count = 0
        sum = 2
        while i < n:
            if is_prime(i):
                print(i)
                count += 1
                sum += i
            i += 2
        print(count)
        return sum

    end = time.time()-start
    print(lowsum(10000), end)
