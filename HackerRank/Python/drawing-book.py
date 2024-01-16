try:
    from raw_input import input
except ImportError:
    pass

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if p == 1 or p == n:
        return 0
    else:
        f_pages = (p // 2)
        b_pages = (n // 2) - (p // 2)
        return f_pages if f_pages <= b_pages else b_pages
        # if int(n / 2) > p:
            # return (n // 2) - (p // 2)
        # else:
            # return ((p // 2) - 1)

if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print(result)