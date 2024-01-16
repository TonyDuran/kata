try:
    from raw_input import input
except ImportError:
    pass

import math
import os
import random
import re
import sys

def plusMinus(arr):
    deno = len(arr)
    pos = float(len([i for i in arr if i > 0])/deno)
    neg = float(len([i for i in arr if i < 0])/deno)
    zero = float(len([i for i in arr if i == 0])/deno)
    print(round(pos, 6))
    print(round(neg, 6))
    print(round(zero, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
