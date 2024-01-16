try:
    from raw_input import input
except ImportError:
    pass

 #list(filter(lambda x: x < d, s))

#!/bin/python3

import os
import sys

import itertools
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards = list(filter(lambda x: x < b, keyboards))
    drives = list(filter(lambda x: x < b, drives))
    closest_result = b
    combinations = [(i,j) for i in keyboards for j in drives]
    # if len(keyboards) >= len(drives):
    #     combinations = [zip(x, drives)for x in itertools.permutations(keyboards, len(drives))]
    # else:
    #     combinations = [zip(x, keyboards)for x in itertools.permutations(drives, len(keyboards))]
    total = -1
    for _  in combinations:
        tmp_sum = sum(_)
        if tmp_sum == b: return b
        elif tmp_sum < b:
            if (b - tmp_sum) < closest_result:
                closest_result = b - tmp_sum
                total = tmp_sum

    return total

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
