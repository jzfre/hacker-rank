#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b number of blacks 3
#  2. INTEGER w number of whites 5
#  3. INTEGER bc cost of black 3
#  4. INTEGER wc cost of white 4
#  5. INTEGER z - tranform
#
def taumBday(b, w, bc, wc, z):
    blacks = 0
    whites = 0

    # convert blacks
    if  (bc + z) < wc:
        whites = w * (bc + z)
    else:
        whites = w * wc

    # convert whites
    if (wc + z) < bc:
        blacks = b * (wc + z)
    else:
        blacks = b * bc

    return blacks + whites

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
