# Poker Hands https://projecteuler.net/problem=54
# User poker.txt in files folder

import time
import numpy as np
from math import factorial as f
from itertools import *

start = time.time()

def AKind(hand, kind):
    num = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    while(len(num) >= kind):
        comp = num[0]
        for x in range(kind):
            
            


def IsFlush(han):
    if(hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]):
        return True
    return False

def IsRoyalFlush(hand):
    royal = [10, 11, 12, 13, 14]
    for x in hand:
        if(not x[0] in royal):
            return False
    return IsFlush(hand)

def IsStraightFlush(hand):
    if(IsFlush(hand)):
        num = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
        numSort = sorted(num)
        if(num[0]+4 == num[1]+3 == num[2]+2 == num[3]+1 == num[4]):
            return max(num[4])
    return 0

def IsFourOfAKind(hand):
    return highCard

def IsFullHouse(hand):
    return highCard

def IsFlush(hand):
    return highCard

def IsStraight(hand):
    return highCard

def IsThreeOfAKind(hand):
    return highCard

def IsTwoPairs(hand):
    return highCard, lowCard, otherCard

def IsPair(hand):
    return highCard

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
        p1+=1
        continue
    if(IsRoyalFlush(p2Hand)):
        p2+=1
        continue
    if(IsStraightFlush(p1Hand) > IsStraightFlush(p2Hand)):
        p1+=1
        continue
    if(IsStraightFlush(p1Hand) < IsStraightFlush(p2Hand)):
        p2+=1
        continue
    if(IsFourOfAKind(p1Hand) > IsFourOfAKind(p2Hand)):
        p1+=1
        continue
    if(IsFourOfAKind(p1Hand) < IsFourOfAKind(p2Hand)):
        p2+=1
        continue
    if(IsFullHouse(p1Hand) > IsFullHouse(p2Hand)):
        p1+=1
        continue
    if(IsFullHouse(p1Hand) < IsFullHouse(p2Hand)):
        p2+=1
        continue
    if(IsFlush(p1Hand) > IsFlush(p2Hand)):
        p1+=1
        continue
    if(IsFlush(p1Hand) < IsFlush(p2Hand)):
        p2+=1
        continue
    if(IsStraight(p1Hand) > IsStraight(p2Hand)):
        p1+=1
        continue
    if(IsStraight(p1Hand) < IsStraight(p2Hand)):
        p2+=1
        continue
    if(IsThreeOfAKind(p1Hand) > IsThreeOfAKind(p2Hand)):
        p1+=1
        continue
    if(IsThreeOfAKind(p1Hand) < IsThreeOfAKind(p2Hand)):
        p2+=1
        continue
    p1TwoPair = IsTwoPairs(p1Hand)
    p2TwoPair = IsFlush(p2Hand)
    if(p1TwoPair[0] > p2TwoPair[0]):
        p1+=1
        continue
    if(p1TwoPair[0] < p2TwoPair[0]):
        p2+=1
        continue
    if(p1TwoPair[1] > p2TwoPair[1]):
        p1+=1
        continue
    if(p1TwoPair[1] < p2TwoPair[1]):
        p2+=1
        continue
    if(p1TwoPair[2] > p2TwoPair[2]):
        p1+=1
        continue
    if(p1TwoPair[2] < p2TwoPair[2]):
        p2+=1
        continue
    if(IsPair(p1Hand) > IsPair(p2Hand)):
        p1+=1
        continue
    if(IsPair(p1Hand) < IsPair(p2Hand)):
        p2+=1
        continue


print("My program took", time.time() - start, "to run.")