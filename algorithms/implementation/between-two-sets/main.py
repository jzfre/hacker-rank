#!/bin/python3

import math
from functools import reduce
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def lcm(a, b):
    return int(a * b / math.gcd(a, b))

def lcms(numbers):
     return reduce(lcm, numbers)

def gcds(numbers):
     return reduce(gcd, numbers)


def getTotalX(a, b):
    print(f'a: {a}, b: {b}')

    # We have first
    firstNum = lcms(a)

    print(f'LCM: {firstNum}')

    totalCnt = 0

    mult = 1
    test = firstNum * mult
    maxSecondArray = max(b)
    # 100 is constraint, dummy but still ok
    # iterate over all multipliers of firstNum
    while test <= maxSecondArray:
        print(f'Testing: {test}')
        fail = False
        # test if current multiplier divides all numbers in array
        for num in b:
            if (num % test != 0):
                fail = True
                print('Fail -> Skipping')

        if not fail:
            totalCnt += 1
        mult += 1
        test = firstNum * mult

    print(f'Total {totalCnt}') 
    return totalCnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
