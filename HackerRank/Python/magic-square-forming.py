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

def _calculate_sides(grid):
    #return a list of all sides
    sides = list()
    sides.extend([sum(x) for x in grid])
    sides.extend([sum(x) for x in zip(*grid)])
    return sides

def _magic_num(sides):
    # return an int for the magic number
    if sides == []:
        return None
    else:
        return max(set(sides), key=sides.count)

def _is_magical(sides):
    return sides == sides[::-1]

def formingMagicSquare(s):
    sides = _calculate_sides(s)
    m_num = _magic_num(sides)
    if _is_magical(sides):
        return 0
    else:
        return 1

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    assert _is_magical(s) == False
    result = formingMagicSquare(s)
    print(result)