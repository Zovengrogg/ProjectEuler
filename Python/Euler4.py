# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the 
# product of two 3-digit numbers.

# TODO Multiply two 3-digit numbers together 
# (Start at 999 x 999 and work down)
array = []
factor1 = []
factor2 = []
for i in range(999, 700, -1):
    for j in range(999, 700, -1):
        palindrome = j*i
        if str(palindrome) == ''.join(reversed(str(palindrome))):
            array.append(palindrome)
            factor1.append(i)
            factor2.append(j)
            break

palindrome = max(array)
a = factor1[array.index(max(array))]
b = factor2[array.index(max(array))]
print(palindrome, a, b)