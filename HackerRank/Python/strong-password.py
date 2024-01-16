try:
    from raw_input import input
except ImportError:
    pass


import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Complete the minimumNumber functio    n below.
def minimumNumber(n, password):
    count = 0
    if not any(e in numbers for e in password):
        password = password + numbers[0]
        count += 1
    if not any(e in lower_case for e in password):
        password = password + lower_case[0]
        count += 1
    if not any(e in upper_case for e in password):
        password = password + upper_case[0]
        count += 1
    if not any(e in special_characters for e in password):
        password = password + special_characters[0]
        count += 1
    if len(password) < 6:
        count += 6 - len(password)

    return count



if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)