#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p == 1:
        return 0
    
    # there should be some math to check whats better approach
    # from behing or from front lol
    half = math.trunc(n / 2)
    if p <= half:
      # from front
      return math.trunc(p / 2)
    else:
      # from back
      return math.trunc(n / 2) - math.trunc(p / 2)

    # 1 % 2 = 0, 1
    # 2 % 2 = 1, 0
    # 3 % 2 = 1, 1
    # 4 % 2 = 2, 0
    # 5 % 2 = 2, 1

    # 1 % 2 = 0, 1
    # 2 % 2 = 1, 0
    # 3 % 2 = 1, 1
    # 4 % 2 = 2, 0
    # 5 % 2 = 2, 1
    # 6 % 2 = 3, 0

    # 1 % 2 = 0, 1
    # 2 % 2 = 1, 0
    # 3 % 2 = 1, 1
    # 4 % 2 = 2, 0
    # 5 % 2 = 2, 1
    # 6 % 2 = 3, 0
    # 7 % 2 = 3, 1
    # 8 % 2 = 4, 0
    # 9 % 2 = 4, 1
    # 10 % 2 = 5, 0
    # 11 % 2 = 5, 1


if __name__ == '__main__':
    n = 6
    p = 2
    
    result = pageCount(n, p)
    print(result)


