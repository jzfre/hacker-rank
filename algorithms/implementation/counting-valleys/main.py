#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleyCnt = 0
    # negative number is valley, 0 - sea level, positive number is hill
    seaLevel = 0

    for step in path:
        # go up
        if (step == 'U'):
              seaLevel += 1
        if (step == 'D'):
            # we going down into valley
            if (seaLevel == 0):
                valleyCnt += 1
            # go down 
            seaLevel -= 1
    
    return valleyCnt

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print('Result', result)
