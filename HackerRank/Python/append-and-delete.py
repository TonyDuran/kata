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

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    com_len = 0
    for _ in range(len(min(s,t))):
        if s[_] == t[_]:
            com_len += 1
        else:
            break
    if (len(s) + len(t)) - (2 * com_len) > k:
        return "No"
    elif (len(s) + len(t) - (2 * com_len)) % 2 ==k%2:
        return "Yes"
    elif len(s) + len(t) - k < 0:
        return "Yes"
    else:
        return "No"


    # count must be <= k to return "Yes"

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)
    print(result)