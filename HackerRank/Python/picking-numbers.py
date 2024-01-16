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

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    highest_arr = 0
    while a:
        count = 1
        prev = a.pop(0)
        for x in a:
            if (x - prev) <= 1:
                count += 1
        if count > highest_arr: highest_arr = count
    return highest_arr

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
