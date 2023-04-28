# Coded Triangle Numbers https://projecteuler.net/problem=42

from math import sqrt
import csv

with open('p042_words.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    words = [i for i in reader]

def isTriangleNumber(n):
    zero1 = (-1+sqrt(1+8*n))/2
    zero2 = (-1-sqrt(1+8*n))/2
    if (zero1.is_integer() and zero1 > 0) or (zero2.is_integer() and zero2 > 0):
        return True
    return False

answers = []
for word in words[0]:
    num_list = [ord(x)-64 for x in word]
    total = 0
    for n in num_list:
        total += n
    if isTriangleNumber(total):
        answers.append(word)

print(len(answers))