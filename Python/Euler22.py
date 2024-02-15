# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import time
import csv

start = time.time()

f = open("p022_names.txt", 'r')
char_num_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                 "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                 "X": 24, "Y": 25, "Z": 26}
names = sorted(f.read().replace('"', '').split(','), key=str)

sum = 0
for index, val in enumerate(names):
    temp = 0
    for x in val:
        temp += char_num_dict[x]
    sum += temp * (index + 1)

print(sum)

end = time.time()

print(end - start)
