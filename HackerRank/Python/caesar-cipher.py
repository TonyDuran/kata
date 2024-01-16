try:
    from raw_input import input
except ImportError:
    pass

import string
from collections import deque
import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    alphabet = string.ascii_letters
    caesar_shift = deque(string.ascii_letters)
    caesar_shift.rotate( - k)
    result = list()
    for _ in s:
        if _ not in alphabet:
            result.append(_)
        else:
            index = alphabet.index(_)
            if index < 26:
                result.append(caesar_shift[alphabet.index(_)].lower())
            elif index < 52 and index > 26:
                result.append(caesar_shift[alphabet.index(_)].upper())
            else:
                result.append(caesar_shift[alphabet.index(_)])
                

    return result

if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)
    print(*result, sep="")