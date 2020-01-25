#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.


def birthday(s, d, m):
    resultsCnt = 0

    # some prelim checks
    if m > len(s):
        # num of months must be count of each square summed together
        # if there is more montsh then total len of array, can't be possible
        # to find some result
        return resultsCnt

    # let iterateover every chocolate square, and find if it
    # meets conditions
    for i in range(len(s)):
        # squareValue is bigger than day of birth, skip
        if s[i] > d:
            continue
        # squareValue is same as day of birth, month of birth must be 1 in that
        # case
        if s[i] == d and m == 1:
            resultsCnt += 1
            continue

        # ok lets find out if we match criteria in sub-loop
        accumulator = 0
        for j in range(m):
            # check indexes
            if (i + j) >= len(s):
                break
            accumulator += s[i+j]
        if accumulator == d:
            resultsCnt += 1

    return resultsCnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
