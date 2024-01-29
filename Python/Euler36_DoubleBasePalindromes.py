# Double Base Palindromes https://projecteuler.net/problem=36

def isDoublePalindrome(n):
    if str(format(n, 'b')) == str(format(n, 'b'))[::-1]:
            return True
    return False

total = 0

for j in range(1, 10):
    for i in range(0, 10):
        for h in range(0, 10):
            num = str(j)+str(i)+str(h)+str(i)+str(j)
            if isDoublePalindrome(int(num)):
                total += int(num)
            num = str(j)+str(i)+str(h)+str(h)+str(i)+str(j)
            if isDoublePalindrome(int(num)):
                total += int(num)
 
for i in range(1, 10):
    for h in range(0, 10):
        num = str(i)+str(h)+str(i)
        if isDoublePalindrome(int(num)):
            total += int(num)
        num = str(i)+str(h)+str(h)+str(i)
        if isDoublePalindrome(int(num)):
            total += int(num)  
    
for h in range(1, 10):
    num = str(h)
    if isDoublePalindrome(int(num)):
        total += int(num) 
    num = str(h)+str(h)
    if isDoublePalindrome(int(num)):
        total += int(num) 


print(total)  