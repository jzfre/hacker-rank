#!/bin/python3

import math
import os
import random
import re
import sys

# this thing always find biggest possible plus, we must also generate
# pluses with smaller size
# check for overlaping whole list -> return max
# dumb bruteforce


def checkPlus(grid, center_x, center_y, pluses):
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
    #print('Max size for plus: ', max_size)

    # just a temp value, we will expect we will find a valid plus
    expectation = True
    plus = {"size": 1, "center": [center_x, center_y],
            "points": [[center_x, center_y]]}
    # check vertical line
    #print('Processing vertical line:')
    for idx in range(center_x - max_size, (center_x + 1) + max_size):
        #print('Processing point: [', idx,  '][', center_y,
              #'] with value: ', grid[idx][center_y])
        if grid[idx][center_y] != 'G':
            expectation = False
            break
        else:
            if [idx, center_y] not in plus["points"]:
                plus["points"].append([idx, center_y])

    # check horizontal line
    if (expectation):
        #print('Processing horizontal line:')
        for idx in range(center_y - max_size, (center_y + 1) + max_size):
            #print('Processing point: [', center_x,  '][',
                  #idx, '] with value: ', grid[center_x][idx])
            if grid[center_x][idx] != 'G':
                expectation = False
                break
            else:
                if [center_x, idx] not in plus["points"]:
                    plus["points"].append([center_x, idx])

    if expectation:
        plus["size"] = (4 * max_size) + 1
        #print('Adding new plus:', plus)
        pluses.append(plus)
        #print('Pluses:', pluses)
        # generate smaller version of pluses
        pluses = generateSmallerPluses(plus, pluses)

        return True

    return False


def generateSmallerPluses(plus, pluses):
    center = plus["center"]
    

    if (plus["size"] == 1):
        return

    size = int(((plus["size"] - 1) / 4))
    
    new_plus = plus.copy()
    
    for new_size in range(size - 1, 0, -1):
        # print('INDEX / NEW SIZE POINT: ', new_size)
        # find min/max X point
        min_x = 16
        top = []
        max_x = -1
        bottom = []
        
        for point in new_plus["points"]:
            if point[0] < min_x:
                min_x = point[0]
                top = point
            if point[0] > max_x:
                max_x = point[0]
                bottom = point
        
        left = [new_plus["center"][0], new_plus["center"][1] - new_size - 1]
        right = [new_plus["center"][0], new_plus["center"][1] + new_size + 1]

        points_to_remove = [top, bottom, left, right]
        # print('Point: ', top, bottom, left, right)
        for point_to_remove in points_to_remove:
            new_points = new_plus["points"].copy()
            if point_to_remove in new_points:
                new_points.remove(point_to_remove)
                new_plus["points"] = new_points

        # Compute new size
        new_plus["size"] = (4 * new_size) + 1
        # print('Adding new plus:', new_plus)
        pluses.append(new_plus.copy())
    
    return pluses

        
def fun(variable, points): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
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
    overlaping = True
    # we need to check every plus with every one, check overlapping
    for first in pluses:
        for second in pluses:
            # check if they are overlap
            if areNotOverlaping(first, second):
                #print(
                    #f'Pluses [{first["center"][0]},{first["center"][1]}] - {first["size"]} and [{second["center"][0]},{second["center"][1]}] - {second["size"]} are not overlapping')
                overlaping = False
                tmp_max_size = first["size"] * second["size"]
                if tmp_max_size > max_size:
                    max_size = tmp_max_size

    # there are multiple pluses in array, all overlaping
    if overlaping:
        overlaping_max_size = 1
        for plus in pluses:
            if plus["size"] > overlaping_max_size:
                overlaping_max_size = plus["size"]

        return overlaping_max_size

    return max_size


def twoPluses(grid):
    #print('### MATRIX ###')
    #print(grid)

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
            #print('Processing center [', x, '][', y, ']')
            if grid[x][y] == 'G':
                checkPlus(grid, x, y, pluses)

    print('Pluses:', pluses)
    return processPluses(pluses)


if __name__ == '__main__':
    fptr = open('./data/input2.txt', 'r')

    nm = fptr.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    #print(n, m)

    grid = []
    for i in range(n):
        grid_row_string = fptr.readline()
        grid_row = list(filter(lambda x: x != '\n', grid_row_string))
        grid.append(grid_row)

    result = twoPluses(grid)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
