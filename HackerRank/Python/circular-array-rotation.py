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
from collections import deque

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    arr_shift = deque(a)
    arr_shift.rotate( k)
    for _ in queries:
        print(arr_shift[_])


if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0]) # number of array elements

    k = int(nkq[1]) # rotation count

    q = int(nkq[2]) # number of queries

    a = list(map(int, input().rstrip().split())) # array elements

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    # print(result)