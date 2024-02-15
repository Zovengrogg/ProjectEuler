# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# a = m^2 - n^2, b = 2mn, c =  m^2 + n^2
done = False
for x in range(1, 50):
    for y in range(1, 50):
        a = y*y - x*x
        b = 2*x*y
        c = x*x + y*y
        if a+b+c == 1000:
            done = True
            break
    if done:
        break
print('a is '+str(a)+'. b is '+str(b)+'. c is '+str(c))
print('The product is '+str(a*b*c))
