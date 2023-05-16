#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    cnt = 0
    for i in str(n):
        d = int(i)
        if d == 0:
            continue
        
        mod = n % d

        if mod == 0:
            cnt += 1

    return cnt

if __name__ == '__main__':
    n = 111
    result = findDigits(n)
    print(result)