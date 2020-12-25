#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
  minVal = min(arr)
  maxVal = max(arr)

  if (minVal >= 0):
    mapperSize = maxVal + 1
  if (minVal < 0):
    mapperSize = minVal + maxVal + 1

  mapper = [0] * mapperSize
  for el in arr:
    mapper[el] += 1
  return mapper

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print('Res: ', result)