try:
    from raw_input import input
except ImportError:
    pass

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_val = sum(arr[:-1])
    max_val = sum(arr[1:])
    print("{} {}".format(min_val, max_val))

if __name__ == '__main__':
    arr = sorted(list(map(int, input().rstrip().split())))

    miniMaxSum(arr)