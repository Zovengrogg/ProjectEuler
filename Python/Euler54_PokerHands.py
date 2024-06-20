# Poker Hands https://projecteuler.net/problem=54
# User poker.txt in files folder

import time
import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()

def IsFlush(hand):
    numSort = SortNum(hand)
    return (hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]), numSort[0]

def IsRoyalFlush(hand):
    numSort = SortNum(hand)
    if numSort[0] == 14 and numSort[1] == 13 and numSort[2] == 12 and numSort[3] == 11 and numSort[4] == 10:
        return IsFlush(hand)[0]
    return False

def IsStraightFlush(hand):
    numSort = SortNum(hand)
    return (IsFlush(hand)[0] and IsStraight(hand)[0]), numSort[0]

def IsFourOfAKind(hand):
    numSort = SortNum(hand)
    if numSort[0] == numSort[1] == numSort[2] == numSort[3]:
        return True, numSort[0]
    if numSort[1] == numSort[2] == numSort[3] == numSort[4]:
        return True, numSort[1]
    return False, numSort[0]

def IsFullHouse(hand):
    return IsThreeOfAKind(hand)[0] and IsPair(hand)[0], IsThreeOfAKind(hand)[1]

def IsStraight(hand):
    numSort = SortNum(hand)
    return numSort[4]+4 == numSort[3]+3 == numSort[2]+2 == numSort[1]+1 == numSort[0], numSort[0]

def IsThreeOfAKind(hand):
    numSort = SortNum(hand)
    return numSort[0] == numSort[1] == numSort[2] or numSort[1] == numSort[2] == numSort[3] or numSort[2] == numSort[3] == numSort[4], numSort[2]

def IsTwoPairs(hand):
    numSort = SortNum(hand)
    if numSort[0] == numSort[1] and numSort[2] == numSort[3]:
        return True, numSort[0], numSort[2], numSort[4]
    if numSort[0] == numSort[1] and numSort[3] == numSort[4]:
        return True, numSort[0], numSort[3], numSort[2]
    if numSort[1] == numSort[2] and numSort[3] == numSort[4]:
        return True, numSort[1], numSort[3], numSort[0] 
    return False, numSort[0], numSort[1], numSort[2]

def IsPair(hand):
    numSort = SortNum(hand)
    conditions = [numSort[0] == numSort[1], numSort[1] == numSort[2], numSort[2] == numSort[3], numSort[3] == numSort[4]]
    if sum(conditions) != 1:
        return False, numSort[0], numSort[1], numSort[2], numSort[3]
    if numSort[0] == numSort[1]:
        return True, numSort[0], numSort[2], numSort[3], numSort[4]
    if numSort[1] == numSort[2]:
        return True, numSort[1], numSort[0], numSort[3], numSort[4]
    if numSort[2] == numSort[3]:
        return True, numSort[2], numSort[0], numSort[1], numSort[4]
    if numSort[3] == numSort[4]:
        return True, numSort[3], numSort[0], numSort[1], numSort[2]

def SortNum(hand):
    num = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    sort = sorted(num)
    numSort = sort[::-1]
    return numSort

loadCards = np.loadtxt('files\poker.txt', dtype="str", delimiter=" ")
dct = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'T':'10', 
'J':'11', 'Q':'12', 'K':'13', 'A':'14', 'D':'1', 'C':'2', 'H':'3', 'S':'4'}

hands = np.zeros((1000, 10, 2))
handNum = 0
for loadHands in loadCards:
    cards =[]
    cardNum = 0
    for card in loadHands:
        hands[handNum][cardNum][0] = dct[card[0]]
        hands[handNum][cardNum][1] = dct[card[1]]
        cardNum += 1
    handNum += 1

p1 = 0
p2 = 0

for hand in hands:
    p1Hand = hand[:5]
    p2Hand = hand[5:]
    if(IsRoyalFlush(p1Hand)): 
        # print(p1Hand, p2Hand, "Royal Flush")
        p1+=1
        continue
    if(IsRoyalFlush(p2Hand)):
        # print(p1Hand, p2Hand, "Royal Flush")
        p2+=1
        continue
    if(IsStraightFlush(p1Hand)[0] and IsStraightFlush(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Straight Flush")
        if(IsStraightFlush(p1Hand)[1] > IsStraightFlush(p2Hand)[1]):
            p1+=1
            continue
        else:
            p2+=1
            continue
    if(IsStraightFlush(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Straight Flush")
        p1+=1
        continue
    if(IsStraightFlush(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Straight Flush")
        p2+=1
        continue
    if(IsFourOfAKind(p1Hand)[0] and IsFourOfAKind(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Four of a Kind")
        if(IsFourOfAKind(p1Hand)[1] > IsFourOfAKind(p2Hand)[1]):
            p1+=1
            continue
        else:
            p2+=1
            continue
    if(IsFourOfAKind(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Four of a Kind")
        p1+=1
        continue
    if(IsFourOfAKind(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Four of a Kind")
        p2+=1
        continue
    if(IsFullHouse(p1Hand)[0] and IsFullHouse(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Full House")
        if(IsFullHouse(p1Hand)[1] > IsFullHouse(p2Hand)[1]):
            p1+=1
            continue
        else:
            p2+=1
            continue
    if(IsFullHouse(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Full House")
        p1+=1
        continue
    if(IsFullHouse(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Full House")
        p2+=1
        continue
    if(IsFlush(p1Hand)[0] and IsFlush(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Flush")
        if(IsFlush(p1Hand)[1] > IsFlush(p2Hand)[1]):
            p1+=1
            continue
        if(IsFlush(p1Hand)[1] < IsFlush(p2Hand)[1]):
            p2+=1
            continue
    if(IsFlush(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Flush")
        p1+=1
        continue
    if(IsFlush(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Flush")
        p2+=1
        continue
    if(IsStraight(p1Hand)[0] and IsStraight(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Straight")
        if(IsStraight(p1Hand)[1] > IsStraight(p2Hand)[1]):
            p1+=1
            continue
        if(IsStraight(p1Hand)[1] < IsStraight(p2Hand)[1]):
            p2+=1
            continue
    if(IsStraight(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Straight")
        p1+=1
        continue
    if(IsStraight(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Straight")
        p2+=1
        continue
    if(IsThreeOfAKind(p1Hand)[0] and IsThreeOfAKind(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Three of a Kind")
        if(IsThreeOfAKind(p1Hand)[1] > IsThreeOfAKind(p2Hand)[1]):
            p1+=1
            continue
        if(IsThreeOfAKind(p1Hand)[1] < IsThreeOfAKind(p2Hand)[1]):
            p2+=1
            continue
    if(IsThreeOfAKind(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Three of a Kind")
        p1+=1
        continue
    if(IsThreeOfAKind(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Three of a Kind")
        p2+=1
        continue
    if(IsTwoPairs(p1Hand)[0] and IsTwoPairs(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Two Pairs")
        if(IsTwoPairs(p1Hand)[1] > IsTwoPairs(p2Hand)[1]):
            p1+=1
            continue
        if(IsTwoPairs(p1Hand)[1] < IsTwoPairs(p2Hand)[1]):
            p2+=1
            continue
        if(IsTwoPairs(p1Hand)[2] > IsTwoPairs(p2Hand)[2]):
            p1+=1
            continue
        if(IsTwoPairs(p1Hand)[2] < IsTwoPairs(p2Hand)[2]):
            p2+=1
            continue
        if(IsTwoPairs(p1Hand)[3] > IsTwoPairs(p2Hand)[3]):
            p1+=1
            continue
        if(IsTwoPairs(p1Hand)[3] < IsTwoPairs(p2Hand)[3]):
            p2+=1
            continue
    if(IsTwoPairs(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Two Pairs")
        p1+=1
        continue
    if(IsTwoPairs(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Two Pairs")
        p2+=1
        continue
    if(IsPair(p1Hand)[0] and IsPair(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Pair")
        if(IsPair(p1Hand)[1] > IsPair(p2Hand)[1]):
            p1+=1
            continue
        if(IsPair(p1Hand)[1] < IsPair(p2Hand)[1]):
            p2+=1
            continue
        if(IsPair(p1Hand)[2] > IsPair(p2Hand)[2]):
            p1+=1
            continue
        if(IsPair(p1Hand)[2] < IsPair(p2Hand)[2]):
            p2+=1
            continue
        if(IsPair(p1Hand)[3] > IsPair(p2Hand)[3]):
            p1+=1
            continue
        if(IsPair(p1Hand)[3] < IsPair(p2Hand)[3]):
            p2+=1
            continue
    if(IsPair(p1Hand)[0]):
        # print(p1Hand, p2Hand, "Pair")
        p1+=1
        continue
    if(IsPair(p2Hand)[0]):
        # print(p1Hand, p2Hand, "Pair")
        p2+=1
        continue
    if(SortNum(p1Hand)[0] > SortNum(p2Hand)[0]):
        # print(p1Hand, p2Hand, "High Card")
        p1+=1
        continue
    if(SortNum(p1Hand)[0] < SortNum(p2Hand)[0]):
        # print(p1Hand, p2Hand, "High Card")
        p2+=1
        continue
    if(SortNum(p1Hand)[1] > SortNum(p2Hand)[1]):
        # print(p1Hand, p2Hand, "High Card")
        p1+=1
        continue
    if(SortNum(p1Hand)[1] < SortNum(p2Hand)[1]):
        # print(p1Hand, p2Hand, "High Card")
        p2+=1
        continue
    if(SortNum(p1Hand)[2] > SortNum(p2Hand)[2]):
        # print(p1Hand, p2Hand, "High Card")
        p1+=1
        continue
    if(SortNum(p1Hand)[2] < SortNum(p2Hand)[2]):
        # print(p1Hand, p2Hand, "High Card")
        p2+=1
        continue
    if(SortNum(p1Hand)[3] > SortNum(p2Hand)[3]):
        # print(p1Hand, p2Hand, "High Card")
        p1+=1
        continue
    if(SortNum(p1Hand)[3] < SortNum(p2Hand)[3]):
        # print(p1Hand, p2Hand, "High Card")
        p2+=1
        continue
    if(SortNum(p1Hand)[4] > SortNum(p2Hand)[4]):
        # print(p1Hand, p2Hand, "High Card")
        p1+=1
        continue
    if(SortNum(p1Hand)[4] < SortNum(p2Hand)[4]):
        # print(p1Hand, p2Hand, "High Card")
        p2+=1
        continue
    print("Error")
print(p1, p2)

print("My program took", time.time() - start, "to run.")