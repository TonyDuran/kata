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

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    result = "NO" if k <= len(list(filter( lambda x: x <= 0,a))) else "YES"
    return result

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)
