#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#
def serviceLane(width, cases):
    result = []

    for case in cases:
        result.append(min(width[case[0]:case[1]+1]))

    return result

if __name__ == '__main__':
    fptr =  sys.stdout

    first_multiple_input = input().rstrip().split()
 
    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    
    result = serviceLane(width, cases)
    print(result)
