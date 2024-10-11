# Cyclical Figurate Numbers https://projecteuler.net/problem=61

import time
from math import sqrt, ceil

start = time.time()

#  Using Quadratic Formula to get range of 4 digit numbers

# print(ceil((sqrt(1 - (4 * 1 * -2000)) - 1)/2))
# print(ceil((sqrt(1 - (4 * 1 * -20000)) - 1)/2))
# print(ceil((sqrt(4 * 1 * 1000) - 1)/2))
# print(ceil((sqrt(4 * 1 * 10000) - 1)/2))
# print(ceil((sqrt(1 - (4 * 3 * -2000)) - 1)/6))
# print(ceil((sqrt(1 - (4 * 3 * -20000)) - 1)/6))
# print(ceil((sqrt(1 - (4 * 2 * -1000)) - 1)/4))
# print(ceil((sqrt(1 - (4 * 2 * -10000)) - 1)/4))
# print(ceil((sqrt(9 - (4 * 5 * -2000)) + 3)/10))
# print(ceil((sqrt(9 - (4 * 5 * -20000)) + 3)/10))
# print(ceil((sqrt(4 - (4 * 3 * -1000)) + 2)/6))
# print(ceil((sqrt(4 - (4 * 3 * -10000)) + 2)/6))


# triangle_numbers = [str(x * (x + 1) // 2)[:2] + 't' + str(x * (x + 1) // 2)[2:] for x in range(45, 141)]
class Link:
    def __init__(self, number, polygonal):
        self.number = number
        self.polygonal = polygonal
        self.first = str(number)[:2]
        self.last = str(number)[-2:]

class Chain:
    def __init__(self, chain):
        self.chain = chain
        self.first = chain[0].first if chain else None
        self.last = chain[-1].last if chain else None


    def combine(self, link):
        if self.first == link.last:
            self.chain[:0] = link
            return True
        if self.last == link.first:
            self.chain.append(link)
            return True
        return False

    def pop(self):
        self.chain = self.chain[:-1]

    def isCyclic(self):
        return self.first == self.last

    def sum(self):
        count = 0
        for x in chain:
            count += x.number
        return count


# def createChain(link_list1, link_list2):
#     chains = []
#     for link1 in link_list1:
#         for link2 in link_list2:
#             if link1.last == link2.first:
#                 chains.append(Chain([link1, link2]))
#             if link1.first == link2.last:
#                 chains.append(Chain([link2, link1]))
#     return chains


# triangle_chains = [Chain([Link(x * (x + 1) // 2, 'triangle')], ['triangle']) for x in range(45, 141)] 
# square_chains = [Chain([Link(x * x, 'square')], ['square']) for x in range(32, 100)] 
# pentagonal_chains = [Chain([Link(x * (3 * x - 1) // 2, 'pentagonal')], ['pentagonal']) for x in range(26, 82)] 
# hexagonal_chains = [Chain([Link(x * (2 * x - 1), 'hexagonal')], ['hexagonal']) for x in range(23, 71)] 
# heptagonal_chains = [Chain([Link(x * (5 * x - 3) // 2, 'heptagonal')], ['heptagonal']) for x in range(21, 64)] 
# octagonal_chains = [Chain([Link(x * (3 * x - 2), 'octagonal')], ['octagonal']) for x in range(19, 59)]

triangle_links = [Link(x * (x + 1) // 2, 'triangle') for x in range(45, 141)] 
square_links = [Link(x * x, 'square') for x in range(32, 100)] 
pentagonal_links = [Link(x * (3 * x - 1) // 2, 'pentagonal') for x in range(26, 82)] 
hexagonal_links = [Link(x * (2 * x - 1), 'hexagonal') for x in range(23, 71)] 
heptagonal_links = [Link(x * (5 * x - 3) // 2, 'heptagonal') for x in range(21, 64)] 
octagonal_links = [Link(x * (3 * x - 2), 'octagonal') for x in range(19, 59)]
                

triangle_numbers = [x * (x + 1) // 2 for x in range(45, 141)]
square_numbers = [x * x for x in range(32, 100)]
pentagonal_numbers = [x * (3 * x - 1) // 2 for x in range(26, 82)]
hexagonal_numbers = [x * (2 * x - 1) for x in range(23, 71)]
heptagonal_numbers = [x * (5 * x - 3) // 2 for x in range(21, 64)]
octagonal_numbers = [x * (3 * x - 2) for x in range(19, 59)]

# triangle_links = [Link(number, 'triangle') for number in triangle_numbers] 
# square_links = [Link(number, 'square') for number in square_numbers] 
# pentagonal_links = [Link(number, 'pentagonal') for number in pentagonal_numbers] 
# hexagonal_links = [Link(number, 'hexagonal') for number in hexagonal_numbers] 
# heptagonal_links = [Link(number, 'heptagonal') for number in heptagonal_numbers] 
# octagonal_links = [Link(number, 'octagonal') for number in octagonal_numbers]

print(triangle_numbers)
print(square_numbers)
print(pentagonal_numbers)
print(hexagonal_numbers)
print(heptagonal_numbers)
print(octagonal_numbers)



# for tlink in triangle_links:
#     chain = Chain(tlink)
#     for slink in square_links:
#         if chain.combine(slink):
#             for plinks in pentagonal_links:
#                 if chain.combine(plink):
#                     for hxlink in hexagonal_links:
#                         if chain.combine(hxlink):
#                             for hplink in heptagonal_links:
#                                 if chain.combine(hplink):
#                                     for olink in octagonal_links:
#                                         if chain.combine(olink):
#                                             if chain.isCyclic():
#                                                 print(chain.sum())
#                                             chain.pop()     
#                                     chain.pop()
#                             chain.pop()
#                     chain.pop()
#             chain.pop()
#     chain.pop()



print("My program took", time.time() - start, "to run.")