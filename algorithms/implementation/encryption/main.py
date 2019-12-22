#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.


def encryption(s):
    # get init values
    strlen = len(s)
    upper = math.ceil(math.sqrt(strlen))
    lower = math.floor(math.sqrt(strlen))

    # dimensions correction
    if (upper * lower < strlen):
        lower += 1

    # generate matrix
    matrix = [['' for i in range(upper)] for i in range(lower)]

    # fill matrix
    for rowIdx in range(lower):
        for colIdx in range(upper):
            if (colIdx + (rowIdx * upper)) < (strlen):

                char = s[colIdx + (rowIdx * upper)]
                matrix[rowIdx][colIdx] = char

    resultString = ''

    # read matrix
    for colIdx in range(upper):
        for rowIdx in range(lower):

            resultString += matrix[rowIdx][colIdx]
        resultString += ' '

    return resultString


if __name__ == '__main__':
    fptr = open('./input.txt', 'r')

    s = fptr.readline()
    print(s)

    result = encryption(s)

    # fptr.write(result + '\n')

    fptr.close()
