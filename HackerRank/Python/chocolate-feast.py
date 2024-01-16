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

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    """
    n: an integer representing Bobby's initial amount of money
    c: an integer representing the cost of a chocolate bar
    m: an integer representing the number of wrappers he can
        turn in for a free bar
    Note: Little Bobby will always turn in his wrappers if
        he has enough to get a free chocolate.
    """
    total = 0
    total = chocolates = int(n / c)
    remaining_wrappers = 0
    while chocolates:
        if chocolates + remaining_wrappers >= m:
            remaining_wrappers, chocolates = (chocolates + remaining_wrappers % m), (chocolates / m)
            total += chocolates
        else:
            chocolates = 0

    return int(total)



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)
        print(result)