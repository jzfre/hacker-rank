#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(numOfCycles):
    currentHeight = 1
    #print(f'NumOfCycles: {numOfCycles}')

    for i in range(1, numOfCycles + 1):
        if (i % 2) == 1:
            currentHeight *= 2
        else:
            currentHeight += 1

    return currentHeight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
