#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    arrLen = len(arr)
    for i in range(arrLen):
        if (arr[i] == V):
            return i



if __name__ == '__main__':
    V = int(input())
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)
    print('Result', result)
