#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
  applesInAreaCnt = 0
  # process apple tree and apples - compute distance
  for applePosition in apples:
    if (applePosition + a >= s) and (applePosition + a <= t):
      applesInAreaCnt += 1

  orangesInAreaCnt = 0
  for orangePosition in oranges:
    if (orangePosition + b >= s) and (orangePosition + b <= t):
      orangesInAreaCnt += 1

  print(applesInAreaCnt)
  print(orangesInAreaCnt)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
