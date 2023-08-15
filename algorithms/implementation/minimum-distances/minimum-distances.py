#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    min = None

    for idi, vali in enumerate(a):
        for idj, valj in enumerate(a):

            if idi != idj and vali == valj:
                possibleMin = abs(idi - idj)
                if min == None:
                  min = possibleMin
                if min > possibleMin:
                  min = possibleMin

    if min == None:
        return -1
    
    return min

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
