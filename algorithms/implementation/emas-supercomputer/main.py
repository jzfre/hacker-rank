#!/bin/python3

import math
import os
import random
import re
import sys

# A LITTLE BIT OPTIMIZED ALGORITHM
# TRIES TO FOUND TWO BIGGEST PLUSES / CROSSES THEN STOPS
# THIS CAN WORK BETTER ON 
# 289

def findBiggestPossibleSize(rows_cnt, cols_cnt):
    max_plus_len = -1

    if rows_cnt > cols_cnt:
        if (rows_cnt % 2):
            max_plus_len = rows_cnt
        else:
            max_plus_len = rows_cnt - 1
    else:
        if (cols_cnt % 2):
            max_plus_len = cols_cnt
        else:
            max_plus_len = cols_cnt - 1

    return max_plus_len


def computeAvailableCenters(rows_cnt, cols_cnt, possible_size):
    centers = []

    rows_iterations_cnt = rows_cnt - possible_size
    cols_iterations_cnt = cols_cnt - possible_size
    print('Iterations: ', rows_iterations_cnt, cols_iterations_cnt)

    row_absolute_middle = 0
    col_absolute_middle = 0

    # get absolute middle for X
    if (rows_cnt % 2):
        row_absolute_middle = [math.ceil(rows_cnt / 2) - 1]
    else:
        tmp = int(rows_cnt / 2)
        row_absolute_middle = [tmp - 1, tmp]

    # get absolute middle for Y
    if (cols_cnt % 2):
        col_absolute_middle = [math.ceil(cols_cnt / 2) - 1]
    else:
        tmp = int(cols_cnt / 2)
        col_absolute_middle = [tmp - 1, tmp]

    # put this result into our array
    # if size of maxtrix is even x odd OR odd x even
    if (len(row_absolute_middle) != len(col_absolute_middle)):
        if (len(row_absolute_middle) > 1):
            centers.append([row_absolute_middle[0], col_absolute_middle[0]])
            centers.append([row_absolute_middle[1], col_absolute_middle[0]])
        else:
            centers.append([row_absolute_middle[0], col_absolute_middle[0]])
            centers.append([row_absolute_middle[0], col_absolute_middle[1]])
    else:
        # are matrix is odd x odd
        if (len(row_absolute_middle) > 1):
            centers.append([row_absolute_middle[0], col_absolute_middle[0]])
            centers.append([row_absolute_middle[0], col_absolute_middle[1]])
            centers.append([row_absolute_middle[1], col_absolute_middle[0]])
            centers.append([row_absolute_middle[1], col_absolute_middle[1]])
        else:
            centers.append([row_absolute_middle[0], col_absolute_middle[0]])

    print('Centers: ', centers)

    if (rows_iterations_cnt > 1) or (cols_iterations_cnt > 1):
        return expandByOuterSize(centers)

    return centers


def expandByOuterSize(centers):

    result = []

    # becuase max size of an array is 15
    min_row = 15
    min_col = 15
    max_row = 0
    max_col = 0

    for point in centers:
        print('Point', point)
        if (point[0] > max_row):
            max_row = point[0]
        if (point[0] < min_row):
            min_row = point[0]
        if (point[1] > max_col):
            max_col = point[1]
        if (point[0] < min_col):
            min_col = point[1]

    # generate other points
    print('MIN MAX', min_row, max_row, min_col, max_col)

    for i in range(min_row - 1, max_row + 2):
        for j in range(min_col - 1, max_col + 2):
            result.append([i, j])

    return result


def checkPlus(center, possiblesize, grid, except_points=False):
    extend_by = math.floor(possiblesize / 2)
    expectation = True
    result = { "val": 1, "points": []}
    print('Checking center: ', center, ' with extend: ', extend_by)
    for x in range(center[0] - extend_by, center[0] + extend_by + 1):
        print('Checking point: [', x, '][', center[1], '] formerly', grid[x][center[1]])
        if except_points and [x, center[1]] in except_points:
          print('Found overlap', [x, center[1]], except_points)
          expectation = False
        result["points"].append([x, center[1]])
        if (grid[x][center[1]] != 'G'):
            expectation = False

    for y in range(center[1] - extend_by, center[1] + extend_by + 1):
        print('Checking point: [', center[0], '][', y, '] formerly', grid[center[0]][y])
        if except_points and [center[0], y] in except_points:
          print('Found overlap', [center[0], y], except_points)
          expectation = False
        result["points"].append([center[0], y])
        if (grid[center[0]][y] != 'G'):
            expectation = False
    if not expectation:
      return expectation

    print('Found cross')  
    result["val"] = (2 * possiblesize) - 1
    print('Result Cross: ', result)
    return result

# Complete the twoPluses function below.


def twoPluses(grid):
    print('### MATRIX ###')
    print(grid)

    rows_cnt = len(grid)
    cols_cnt = len(grid[0])

    print('### MAX PLUS LEN ###')
    max_possible_size = findBiggestPossibleSize(rows_cnt, cols_cnt)
    print(max_possible_size)

    # try to find two biggest pluses
    first_plus = { "val": 1, "points": []}
    second_plus = { "val": 1, "points": []}

    # try to find plus with horizontal/vertical size 7, then 5 ... until size 3
    # as you can see step is -2, there is no need to find size 1 as this results to
    # result 1 :):

    for possible_size in range(max_possible_size, 1, -2):
        print('Possible size', possible_size)
        centers = computeAvailableCenters(rows_cnt, cols_cnt, possible_size)
        print('Centers for size: ', possible_size, ' are: ', centers)

        for center in centers:

            if first_plus["val"] == 1:
              plus_result = checkPlus(center, possible_size, grid)
            else:
              plus_result = checkPlus(center, possible_size, grid, first_plus["points"])

            plus_result = checkPlus(center, possible_size, grid)

            if (plus_result) and (first_plus["val"] == 1):
                first_plus = plus_result
                print('First FOUND');
                continue
            if (plus_result) and (second_plus["val"] == 1):
                second_plus = plus_result
                print('Second FOUND')
                break


    return first_plus["val"] * second_plus["val"]


if __name__ == '__main__':
    fptr = open('./data/input02.txt', 'r')

    nm = fptr.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    print(n, m)

    grid = []
    for i in range(n):
        grid_row_string = fptr.readline()
        grid_row = list(filter(lambda x: x != '\n', grid_row_string))
        grid.append(grid_row)

    result = twoPluses(grid)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
