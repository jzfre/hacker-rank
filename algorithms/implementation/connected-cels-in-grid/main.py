#!/bin/python3

import math
import os
import random
import re
import sys

toProc = []

def findAdjacentCels(matrix):
    rowCnt = len(matrix)
    colCnt = len(matrix[0])
    outerIndexes = [[-1, 0], [-1, 1], [0, 1],
                    [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    shouldReset = True

    for tp in toProc: 
        for index in outerIndexes:
            # compute indexes
            oi = tp[0] + index[0]
            oj = tp[1] + index[1]
            if (oi >= 0 and oi < rowCnt) and (oj >= 0 and oj < colCnt) and matrix[oi][oj] == 1:
                if [oi, oj] not in toProc:
                    shouldReset = False
                    toProc.append([oi, oj])

    if shouldReset:
        toProc.clear

    return len(toProc)


# Complete the connectedCell function below.
# DUMMY - iterate over each cell in matrix,
# find out if they are connected
# create list of connected areas
def connectedCell(matrix):
    results = [0]

    rowCnt = len(matrix)
    colCnt = len(matrix[0])

    # iterate over every cell
    for i in range(rowCnt):
        for j in range(colCnt):
            if matrix[i][j] == 1:
                toProc.append([i, j])
                results.append(findAdjacentCels(matrix))
                toProc.clear()

    return max(results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
