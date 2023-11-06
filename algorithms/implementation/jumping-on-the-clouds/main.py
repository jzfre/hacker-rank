#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    arr_len = len(c)
    count = 0  
    index = 0
    while index < arr_len:
        print('Index', index)
        if index == arr_len - 1:
            break

        if index + 2 < arr_len and c[index+2] == 1:
            count = count + 1
            index = index + 1
            continue
        
        if index + 2 < arr_len and c[index+2] == 0:
            count = count + 1
            index = index + 2
            continue

        if index + 1 < arr_len and c[index+1] == 1:
            count = count + 1
            index = index + 2
            continue
        
        if index + 1 < arr_len and c[index+1] == 0:
            count = count + 1
            index = index + 1
            continue
        
    return count


if __name__ == '__main__':
    fptr = sys.stdout  

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
