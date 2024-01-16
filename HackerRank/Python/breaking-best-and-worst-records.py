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

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest_score = highest_score = 0
    lowest_record = highest_record = 0
    for x,v in enumerate(scores):
        # initialize scores
        if x == 0:
            lowest_score = highest_score = v
            continue

        if v > highest_score:
            highest_record += 1
            highest_score = v
            continue
        
        if v < lowest_score:
            lowest_record += 1
            lowest_score = v


    return highest_record, lowest_record


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(*result, sep=" ")
