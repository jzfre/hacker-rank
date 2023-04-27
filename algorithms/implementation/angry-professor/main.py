#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#


def angryProfessor(k, a):
    # Write your code here
    on_time_cnt = 0
    for at in a:
        #print('Num:', at)
        if at <= 0:
            on_time_cnt += 1
            #print('Current cnt: ', cnt)

    if on_time_cnt < k:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
