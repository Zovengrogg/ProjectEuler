# You are given the following information,
# but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# To check if the first of the month is a sunday I will use the counter mod 7
# Sunday = 0 mod 7 or in other words counter % 7 == 0
# This is because I set the counter to the year 1901 and added 1 to it so that
# it is 0 mod 7 rather than 6 mod 7
counter = 367
sunday = 0


def check(x):
    global counter
    global sunday
    if counter % 7 == 0:
        sunday += 1
    counter += x


for year in range(1901, 2001):
    if year % 4 == 0:
        leap = True
    else:
        leap = False
    if year % 100 == 0 and year % 400 != 0:
        leap = False
    # Jan
    check(31)
    # Feb
    if leap:
        check(29)
    else:
        check(28)
    # Mar
    check(31)
    # Apr
    check(30)
    # May
    check(31)
    # Jun
    check(30)
    # Jul
    check(31)
    # Aug
    check(31)
    # Sep
    check(30)
    # Oct
    check(31)
    # Nov
    check(30)
    # Dec
    check(31)

print(sunday)

