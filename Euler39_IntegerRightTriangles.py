# Integer Right Triangles https://projecteuler.net/problem=39

import time

start = time.time()

a = 1
b = 1
c = 1
p = 0
rightTriangles = []
while p < 1000:
    while p < 1000:
        while p < 1000:
            c += 1
            p = a + b + c
            if a*a + b*b == c*c and p < 1000:
                rightTriangles.append(p)
        b += 1
        c = b
        p = a + b + c
    a += 1
    b = a
    c = a
    p = a + b + c
print(max(set(rightTriangles), key = rightTriangles.count))
print("My program took", time.time() - start, "to run.")