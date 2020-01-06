#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    # lets analyze starting points

    # they have same speed rate (so we will get division by zero on next lines)
    # they have different starting points, they will never be in same point
    if (v1 == v2) and (x1 != x2):
        return 'NO'

    # they match in first jump, also this handles case when they have same speeds and same starting
    # points
    if (x1 + v1) == (x2 + v2):
        return 'YES'

    result = (x1 - x2) / (v2 - v1)
    frac, whole = math.modf(result)
    # result is number of steps it must be positive integer we want to return 'YES'
    if frac == 0.0 and int(whole) > 0:
        return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
