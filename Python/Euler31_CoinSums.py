# Coin Sums https://projecteuler.net/problem=31

# ways = 0

# ones = 200
# twos = 0
# fives = 0
# tens = 0
# twenties = 0
# fifties = 0
# onehundreds = 0
# twohundreds = 0

# while ones != 0:
#     while ones != 0:
#         while ones != 0:
#             # ISSUE
#             while ones != 0 and ones != 10:
#                 while ones != 0:
#                     while ones != 0:
#                         # ISSUE
#                         while ones != 0 and ones != 1:
#                             ones -= 2
#                             ways += 1
#                         fives += 1
#                         ways += 1
#                         ones = 200 - 5*fives - 10*tens - 20*twenties - 50*fifties - 100*onehundreds- 200*twohundreds
#                     fives = 0
#                     tens += 1
#                     ways += 1
#                     ones = 200 - 5*fives - 10*tens - 20*twenties - 50*fifties - 100*onehundreds- 200*twohundreds
#                 tens = 0
#                 twenties += 1
#                 ways += 1
#                 ones = 200 - 5*fives - 10*tens - 20*twenties - 50*fifties - 100*onehundreds- 200*twohundreds
#             twenties = 0
#             fifties += 1
#             ways += 1
#             ones = 200 - 5*fives - 10*tens - 20*twenties - 50*fifties - 100*onehundreds- 200*twohundreds
#         fifties = 0
#         onehundreds += 1
#         ways += 1
#         ones = 200 - 5*fives - 10*tens - 20*twenties - 50*fifties - 100*onehundreds- 200*twohundreds
#     onehundreds = 0
#     twohundreds += 1
#     ways += 1
#     ones = 200 - 5*fives - 10*tens - 20*twenties - 50*fifties - 100*onehundreds- 200*twohundreds
# print(ways)

target  = 200
ways = 0
 
# for (a == target, a >= 0):
#     a -= 200
#     for (int b = a; b >= 0; b -= 100) {
#         for (int c = b; c >= 0; c -= 50) {
#             for (int d = c; d >= 0; d -= 20) {
#                 for (int e = d; e >= 0; e -= 10) {
#                     for (int f = e; f >= 0; f -= 5) {
#                         for (int g = f; g >= 0; g -= 2) {
#                             ways++;
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }
a = target
while  a >= 0:
    b = a
    while b >= 0:
        c = b
        while c >= 0:
             d = c
             while d >= 0:
                 e = d
                 while e >= 0:
                     f = e
                     while f >= 0:
                        g = f
                        while g >= 0:
                            ways += 1
                            g -= 2
                        f -= 5
                     e -= 10
                 d -= 20
             c -= 50
        b -= 100
    a -= 200
print(ways)