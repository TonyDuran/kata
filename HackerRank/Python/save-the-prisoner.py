try:
    from raw_input import input
except ImportError:
    pass

import math
import os
import random
import re
import sys
from collections import deque

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    candy_rem = (m % n) - 1
    result = n if (s + candy_rem) % n == 0 else (s + candy_rem) % n
    return result

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        print(result)