#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.

# dummy analytical solution


def happyLadybugs(bugList):
    print(bugList)

    classifier = {}

    # let's build a classifier first
    for bug in bugList:
        if bug in classifier:
            classifier[bug] += 1
        else:
            classifier[bug] = 1

    # if there is only one ladybug of specidied color, return no
    for color in classifier:
        if classifier[color] == 1 and color != '_':
            return 'NO'

    if '_' in classifier and classifier['_'] >= 1:
        return 'YES'

    # we can't jump iterate over whole board and find if ladybugs are happy
    for bugIdx in range(len(bugList)):
        if bugList[bugIdx] == '_':
            continue

        if (bugIdx == 0) and bugList[bugIdx] != bugList[bugIdx + 1]:
            return 'NO'
        
        if (bugIdx == (len(bugList) - 1)) and bugList[bugIdx] != bugList[bugIdx - 1]:
            return 'NO'

        if (bugList[bugIdx] != bugList[bugIdx - 1] and bugList[bugIdx] != bugList[bugIdx + 1]):
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
