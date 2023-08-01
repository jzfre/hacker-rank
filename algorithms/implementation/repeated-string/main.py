#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
def repeatedString(s, n):
    a_char_indexes = [0] * 100
    total_a_in_s = 0
    for idx, ch in enumerate(s):
        if ch == 'a':
            a_char_indexes[idx] = 1
            total_a_in_s += 1
    
    if total_a_in_s == 0:
        return 0

    d = n // len(s)
    sp = n % len(s)

    acc = d * total_a_in_s
    if (sp != 0):
        acc += sum(a_char_indexes[0: sp])

    return acc

if __name__ == '__main__':
    s = 'a'

    n = 10000

    result = repeatedString(s, n)
    print('Result:', result)
