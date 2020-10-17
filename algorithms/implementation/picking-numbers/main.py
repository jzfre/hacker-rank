#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    # Write your code here
    registryLen = 100
    registry = registryLen * [0]
    result = 0
    maxTuple = 0
    curTuple = 0

    # Create a registry that counts the numbers under indexes
    for num in a:
        registry[num] += 1

    # Resolve the problem by checking if tuples in array has max 
    for idx in range(registryLen):
        if (idx + 1 >= registryLen):
            break

        curTuple = registry[idx] + registry[idx+1]
        if (curTuple > maxTuple):
            maxTuple = curTuple

    return maxTuple

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print('Result:', result)
