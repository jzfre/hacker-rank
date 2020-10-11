#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.

MOVE = 97

def designerPdfViewer(h, word):
    heights = []
    # lets create array with heights
    for letter in word:
        heights.append(h[ord(letter) - MOVE])

    # return len of string * max height
    result = len(heights) * max(heights)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
