#!/bin/python3

import math
import os
import random
import re
import sys


def checkPlus(grid, center_x, center_y):
    # rows count of the grid
    rows_cnt = len(grid)
    # cols count of the grid
    cols_cnt = len(grid[0])

    max_size_top = center_y
    max_size_right = (cols_cnt - 1) - center_y
    max_size_bottom = (rows_cnt - 1) - center_x
    max_size_left = center_x

    max_size = min(max_size_top, max_size_right,
                   max_size_bottom, max_size_left)
    print('Max size for plus: ', max_size)

    # just a temp value, we will expect we will find a valid plus
    expectation = True
    plus = {"size": 1, "center": [center_x, center_y],
            "points": [[center_x, center_y]]}
    # check vertical line
    print('Processing vertical line:')
    for idx in range(center_x - max_size, (center_x + 1) + max_size):
        print('Processing point: [', idx,  '][', center_y,
              '] with value: ', grid[idx][center_y])
        if grid[idx][center_y] != 'G':
            expectation = False
            break
        else:
            if [idx, center_y] not in plus["points"]:
                plus["points"].append([idx, center_y])

    # check horizontal line
    if (expectation):
        print('Processing horizontal line:')
        for idx in range(center_y - max_size, (center_y + 1) + max_size):
            print('Processing point: [', center_x,  '][',
                  idx, '] with value: ', grid[center_x][idx])
            if grid[center_x][idx] != 'G':
                expectation = False
                break
            else:
                if [center_x, idx] not in plus["points"]:
                    plus["points"].append([center_x, idx])

    if expectation:
        plus["size"] = (4 * max_size) + 1
        return plus

    return False


def areNotOverlaping(first, second):
    for i in first["points"]:
        for j in second["points"]:
            if i == j:
                return False
    return True


def processPluses(pluses):
    # there is only one plus, we can return it
    if len(pluses) == 1:
        return pluses[0]["size"]

    max_size = 1

    # we need to check every plus with every one, check overlapping
    for first in pluses:
        for second in pluses:
            # check if they are overlap
            if areNotOverlaping(first, second):
                print(f'Pluses [{first["center"][0]},{first["center"][1]}] and [{second["center"][0]},{second["center"][1]}] are not overlapping')
                tmp_max_size = first["size"] * second["size"]
                if tmp_max_size > max_size:
                    max_size = tmp_max_size

    return max_size


def twoPluses(grid):
    print('### MATRIX ###')
    print(grid)

    # rows count of the grid
    rows_cnt = len(grid)
    # cols count of the grid
    cols_cnt = len(grid[0])

    pluses = []

    # we are going to find all possible pluses with size > 5
    # we are not processing border points
    for x in range(1, rows_cnt - 1):
        for y in range(1, cols_cnt - 1):
                # skip if value is BAD, this cant be cross
            print('Processing center [', x, '][', y, ']')
            if grid[x][y] == 'G':
                result = checkPlus(grid, x, y)
                if result:
                    pluses.append(result)

    print('Pluses:')
    print(pluses)
    return processPluses(pluses)


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
