# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Takes input for which numbers to use as multiples
x = input("First multiple: ")
y = input("Second multiple: ")
max = input("Sum below: ")
# Declare variable
x = int(x)
y = int(y)
max = int(max)
sum = 0
for w in range(x,max, x):
    sum += w
    print(w)
for w in range(y, max, y):
# If w is a multiple of x we already added it    
    if w%x == 0:
        continue
    print(w)
    sum += w
print(sum)