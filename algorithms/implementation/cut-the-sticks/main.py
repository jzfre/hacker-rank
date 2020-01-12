#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):
    returnArray = []
    nextArray = arr[:]

    while (len(nextArray) > 0):
        currentArray = nextArray[:]

        # reset "to be processed array"
        nextArray.clear()

        # counter of removed elements
        removedElemsCnt = 0

        currentArrayLen = len(currentArray)
        for i in range(currentArrayLen):
                # find lowest value
                minValue = min(currentArray)
                # save current value
                currentValue = currentArray[i]

                difference = currentValue - minValue
                if difference != 0:
                    nextArray.append(difference)

        returnArray.append(currentArrayLen)

    return returnArray


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
