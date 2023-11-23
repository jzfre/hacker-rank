#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

# 1 2 4 5 7 8 10
# i - 1
# if + = d, ok,


def beautifulTriplets(d, arr):
    # Write your code here
    #print('d', d, 'arr', arr)
    arr_len = len(arr)
    cnt = 0
    # must have at least three elements
    if arr_len < 3:
        return cnt

    for i in range(0, arr_len - 2):
        #print('i', i, 'iv', arr[i])
        for j in range(i + 1, arr_len - 1):
            #print('j', j, 'jv', arr[j])
            if arr[i] + d == arr[j]:
                for k in range(j+1, arr_len):
                    #print('k', k, 'kv', arr[k])
                    if arr[j] + d == arr[k]:
                        cnt += 1
                    else:
                        continue
            else:
                continue

    return cnt


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
