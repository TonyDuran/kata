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

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a_distance = abs(z - x)
    cat_b_distance = abs(z - y)
    if cat_a_distance == cat_b_distance:
        return "Mouse C"
    if cat_a_distance < cat_b_distance:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)
