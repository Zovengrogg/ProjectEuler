# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

single = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

count = 0
# Digits before 100
for name in single:
    for letter in name:
        count += 1
for name in teens:
    for letter in name:
        count += 1
for name in tens:
    prefix = 0
    for letter in name:
        prefix += 1
    count += prefix
    for z in single:
        for letter in z:
            count += 1
        count += prefix

# Digits after 100
for hundred in range(0, 9):
    hundred_and = 0
    for x in single[hundred]:
        count += 1
        hundred_and += 1
    count += 7
    hundred_and += 10
    for name in single:
        count += hundred_and
        for letter in name:
            count += 1
    for name in teens:
        count += hundred_and
        for letter in name:
            count += 1
    for name in tens:
        prefix = 0
        for letter in name:
            prefix += 1
        count += hundred_and
        count += prefix
        for z in single:
            count += hundred_and
            for letter in z:
                count += 1
            count += prefix
# 1000
count += 11
print(count)
