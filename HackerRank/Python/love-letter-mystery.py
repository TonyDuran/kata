try:
    from raw_input import input
except ImportError:
    pass

#!/bin/python3

import math
import os
import random
import re
import sys
import string
alphabet = string.ascii_lowercase
# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    first_half = s[:len(s)//2]
    first_half = first_half[::-1]  
    second_half = s[len(s)//2:] if len(s) % 2 == 0 else s[len(s)//2+1:] 
    count = 0
    for x in range(len(first_half)):
        if alphabet.index(first_half[x]) < alphabet.index(second_half[x]):
            count += alphabet.index(second_half[x]) - alphabet.index(first_half[x])
        elif alphabet.index(first_half[x]) > alphabet.index(second_half[x]):
            count += alphabet.index(first_half[x]) - alphabet.index(second_half[x])
        else:
            continue
    return count
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)
        print(result)

