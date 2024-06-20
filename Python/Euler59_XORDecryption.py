# XOR Decryption https://projecteuler.net/problem=59

import time
import numpy as np
# from math import factorial as f
from itertools import *

start = time.time()

cipher = np.loadtxt('files\\0059_cipher.txt', dtype="str", delimiter=",")
cipher = [int(i) for i in cipher]

#97-112
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            key = [a, b, c]
            message = []
            for i in range(0, len(cipher), 3):
                for j in range(3):
                    message.append(cipher[i+j] ^ key[j])
            message = ''.join([chr(i) for i in message])
            if 'the' in message and 'and' in message and 'from' and 'to' in message:
                print(message)
                print(sum([ord(i) for i in message]))
                break
    else:
        continue
    break

print("My program took", time.time() - start, "to run.")