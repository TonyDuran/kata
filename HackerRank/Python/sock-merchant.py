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

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dist_vals = set(ar)
    count = 0
    for x in dist_vals:
        if ar.count(x) < 2:
            continue
        else:
            count += int(ar.count(x) / 2)

    return count

if __name__ == '__main__':
    num = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = sockMerchant(num, arr)
    print(result)
