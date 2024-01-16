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

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    full_split = sum(bill) / 2
    bill.pop(k)
    fair_split = sum(bill) / 2
    if int(fair_split) == b:
        print("Bon Appetit")
    else:
        print(int(b - fair_split))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)