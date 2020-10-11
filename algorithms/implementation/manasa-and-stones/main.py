#!/bin/python3

import math
import os
import random
import itertools
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    # generate all variations
    variations = list(itertools.combinations_with_replacement([a, b], n - 1))

    # make computing
    rawResult = []

    for variation in variations:
        computed = 0
        for value in variation:
            computed += value
        rawResult.append(computed)

    # sort array 
    rawResult.sort()

    # remove non unique values
    result = []

    for value in rawResult:
        if value not in result:
            result.append(value)

    print(result)
  
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()