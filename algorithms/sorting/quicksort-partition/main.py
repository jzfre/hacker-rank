#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
  pivot = arr[0];
  left = []
  equal = []
  right = []
  for el in arr:
    if (el < pivot):
      left.append(el)
    if (el == pivot):
      equal.append(el)
    if (el > pivot):
      right.append(el)
  
  result = left + equal + right
  return " ".join(map(str,result))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print('Result', result)

