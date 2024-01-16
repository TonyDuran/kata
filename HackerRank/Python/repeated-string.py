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

# Complete the repeatedString function below.
def repeatedString(s, n):
    occurences = (n // len(s)) * s.count('a')
    remainder = s[:(n % len(s))].count('a')
    return occurences + remainder
    # iterations = s * n
    # return iterations[:n].count('a')

if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)