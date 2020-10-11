#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.


def missingNumbers(new, origin):

    originLen = len(origin)
    newLen = len(new)

    # TODO is this true?
    if originLen == newLen:
        return []

    # we shoul iterate over origin array, so we fill missing numbers
    # in new array with zeroes
    lenDiff = originLen - newLen

    decoratedNew = new.copy()

    # for i in range(lenDiff):
    #     decoratedNew.append(10001)

    decoratedNewLen = len(decoratedNew)

    missing = []

    sortedOrigin = sorted(origin)
    sortedDecoratedNew = sorted(decoratedNew)

    # print(f'Origin: {sortedOrigin}')
    # print(f'New___: {sortedDecoratedNew}')

    missingCnt = 0

    for i in range(originLen):
        # LOL
        if  i <=  (len(sortedDecoratedNew) - 1):
          if (sortedOrigin[i] != sortedDecoratedNew[i]):
              missingCnt += 1
              # found difference
              print(f'Missing no. {missingCnt}')
              print(f'Index: {i}, Decorated Len: {len(sortedDecoratedNew)}')
              print(
                  f'Found difference {sortedOrigin[i]}, {sortedDecoratedNew[i]}')
              if sortedOrigin[i] not in missing:
                  missing.append(sortedOrigin[i])
              sortedDecoratedNew.insert(i, 0)
              print(f'New Decorated Len: {len(sortedDecoratedNew)}')
        else: 
          missing.append(sortedOrigin[i])


    print(f'Missing: {missing}')
    return missing



if __name__ == '__main__':
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    n=int(input())

    arr=list(map(int, input().rstrip().split()))

    m=int(input())

    brr=list(map(int, input().rstrip().split()))

    result=missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
