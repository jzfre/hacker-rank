#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
# x - CatA position
# y - CatB position
# z - Mouse C position


def catAndMouse(x, y, z):
    catAVsMouseLen = abs(x-z)
    catBVsMouseLen = abs(y-z)

    if (catBVsMouseLen < catAVsMouseLen):
        return 'Cat B'
    elif (catAVsMouseLen < catBVsMouseLen):
        return 'Cat A'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open('output01.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')

    fptr.close()
