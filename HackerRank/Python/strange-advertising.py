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

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    count = 0
    start = 5
    for _ in range(n):
        count += int(start / 2)
        start = int(start/2) * 3
    return count

if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)
    print(result)