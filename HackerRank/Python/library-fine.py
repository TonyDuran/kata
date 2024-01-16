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

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    """
    [d,m,y]1 == date the book was returned
    [d,m,y]2 == due date for the book
    inputs are treated as strings first (lazy comparisons)

    """
    fine = 0
    if int(y1 + m1 + d1) <= int(y2 + m2 + d2):
        return fine
    else:
        if int(y1) > int(y2):
            fine = 10000
        else:
            if int(m1) > int(m2):
                fine = (int(m1) - int(m2)) * 500
            else:
                fine = (int(d1) - int(d2)) * 15
    return fine
if __name__ == '__main__':
    d1M1Y1 = input().split()

    d1 = str(d1M1Y1[0]).zfill(2)

    m1 = str(d1M1Y1[1]).zfill(2)

    y1 = d1M1Y1[2]

    d2M2Y2 = input().split()

    d2 = str(d2M2Y2[0]).zfill(2)

    m2 = str(d2M2Y2[1]).zfill(2)

    y2 = d2M2Y2[2]

    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
