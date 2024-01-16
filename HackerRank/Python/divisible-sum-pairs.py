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

from itertools import combinations
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    pairs = list(combinations(ar,2))
    count = 0
    for _ in pairs:
        if sum(_) % k == 0:
            count += 1

    return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)