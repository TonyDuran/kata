try:
    from raw_input import input
except ImportError:
    pass

import math
import os
import random
import re
import sys

from string import ascii_lowercase
# Complete the designerPdfViewer function below.
alphabet = ascii_lowercase
from operator import itemgetter

def designerPdfViewer(alpha_dict, word):
    values = itemgetter(*word)(alpha_dict)
    return len(word) * (max(values))

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))
    alpha_dict = dict(zip(alphabet, h))

    word = input()

    result = designerPdfViewer(alpha_dict, word)
    print(result)
