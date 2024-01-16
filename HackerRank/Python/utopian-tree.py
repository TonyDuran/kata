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

# Complete the utopianTree function below.
def utopianTree(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    height = 0
    for x in range(n + 1):
        if x % 2 == 0:
            height += 1
        else:
            height =  2 * height
    return height

if __name__ == '__main__':

    t = int(input())

    for txitr in range(t):
        n = int(input())

        result = utopianTree(n)
        print(result)

