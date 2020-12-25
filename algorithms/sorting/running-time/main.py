#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.


def runningTime(arr):
    shiftCnt = 0
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            shiftCnt +=1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return shiftCnt


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    print('Result', result)
