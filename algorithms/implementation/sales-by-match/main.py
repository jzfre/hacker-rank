#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sortedSocks = sorted(ar)
    pairsCnt = 0
    idx = 0

    while (idx + 1) < n:
        if sortedSocks[idx] == sortedSocks[idx + 1]:
            pairsCnt += 1
            idx += 2 # because we can skip another one (because thats a pair)
        else:
            idx += 1

    return pairsCnt

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print('Result:', result)
