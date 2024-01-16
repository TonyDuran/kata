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

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_total = 0
    current_level = 0
    in_valley = False
    for x in s:

        if current_level < 0:
            in_valley = True

        if x == "U":
            current_level += 1
        elif x == "D":
            current_level -= 1

        if in_valley:
            if current_level == 0:
                valley_total += 1
                in_valley = False

    return valley_total

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)