#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.


# don't know if list of prices is sorted
# he vants indexes based on prices, so 
# we do dummy n^2 solution

# we could find lowest price and then 
# remove all prices bigger than (currentPrice - lowestPrice) > m
# mon

def icecreamParlor(m, arr):
    arrLen = len(arr)
    for i in range(arrLen):
        for j in range(arrLen):
            # they cant buy same flavour
            if i == j:
                continue
            if (arr[i] + arr[j]) == m:
                #found a solution return indexes
                return [i+1, j+1]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
