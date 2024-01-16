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

def getDigit(number, n):
    return number // 10**n % 10

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    for x in range(len(str(n))):
        d = getDigit(n, x)
        if d == 0:
            continue
        elif n % d == 0:
            count += 1
    return count
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)
        print(result)
