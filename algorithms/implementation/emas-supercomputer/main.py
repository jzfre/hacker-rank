#!/bin/python3

import math
import os
import random
import re
import sys


def checkPlus(center_x, center_y, grid):
    print('ARGS: ', center_x, center_y)

    rows_cnt = len(grid)
    cols_cnt = len(grid[0])

    min_left_idx = 0
    max_right_idx = cols_cnt - 1
    min_top_idx = 0
    max_bottom_idx = rows_cnt

    current_x = center_x
    current_y = center_y

    plus = {"size": 0, "points": []}

    # check left side
    while(current_x > )

# extremely dumb solution
def twoPluses(grid):
    print('### MATRIX ###')
    print(grid)

    rows_cnt = len(grid)
    cols_cnt = len(grid[0])

    pluses = []

    first_plus = {"size": 1, "points": []}
    second_plus = {"size": 1, "points": []}

    # first of all get all pluses
    for x in range(1, rows_cnt):
        for y in range(1, cols_cnt):
            if (grid[x][y] != 'G'):
              continue
            result = checkPlus(x, y, grid)
            if result:
                pluses.append(result)

    print('Pluses', pluses)

    if (first_plus["size"] == 1) and (second_plus["size"] == 1):
        return 1
    else:
        return first_plus["size"] + second_plus["size"] - 1


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
