#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
def beautifulDays(i, j, k):
    # Write your code here
    cnt = 0
    for n in range(i, j + 1):
        res = abs(n - int(str(n)[::-1])) / k
        if res.is_integer():
            cnt += 1
          
    return cnt

if __name__ == '__main__':
    i = 13
    j = 43
    k = 3

    result = beautifulDays(i, j, k)
    print(result)
