#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    brokenMin = 0
    brokenMax = 0
    brokenMinCnt = 0
    brokenMaxCnt = 0
    firstIteration = True


    for result in scores:
        if firstIteration:
            brokenMin = result
            brokenMax = result
            firstIteration = False
        else:
            if result < brokenMin:
                brokenMin = result
                brokenMinCnt += 1
            if result > brokenMax:
                brokenMax = result
                brokenMaxCnt += 1
    
    return(brokenMaxCnt,brokenMinCnt)

if __name__ == '__main__':

    n = int(input())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
