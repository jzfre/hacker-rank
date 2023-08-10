#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def equalizeArray(arr):
    hash_map = {}

    max_count = None
    max_item = None

    # Write your code here
    for item in arr:
        count = hash_map.get(item, 0) + 1

        if not max_count or count > max_count:
            max_count = count
            max_item = item

        hash_map[item] = count

    deletions = 0

    for key in hash_map:
        if key != max_item:
            deletions += hash_map[key]
        
    return deletions


if __name__ == '__main__':
    print(equalizeArray([1, 2, 2, 2, 4, 1, 4, 5, 5, 6, 7, 2]))
