try:
    from raw_input import input
except ImportError:
    pass

#!/bin/python3

import math
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(n-m+1):
        if(sum(s[i:m+i])==d):
            count = count + 1
    return count


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)
