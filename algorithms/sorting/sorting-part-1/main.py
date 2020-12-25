#!/bin/python3

import math
import os
import random
import re
import sys

def arrPrint(arr):
  for i in arr:
    print(i, end = ' ')
  print()

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
  toTest = arr[n-1]
  for i in range(n - 1, -1, -1):
    if (i == 0):
      arr[i] = toTest
      arrPrint(arr)
      break
    if (toTest < arr[i-1]):
      arr[i] = arr[i-1]
      arrPrint(arr)
    else:
      arr[i] = toTest
      arrPrint(arr)
      break


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)