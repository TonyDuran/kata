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

# Complete the staircase function below.
def staircase(n):
    for _ in range(1,n+1): 
        print((_ * "#").rjust(n," ")) 

if __name__ == '__main__':
    n = int(input())

    staircase(n)
