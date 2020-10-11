#!/usr/local/bin/python3

import math
import time
import os
import random
import re
import sys

# Complete the migratoryBirds function below.


def migratoryHashMap(arr):
    birdHashMapHu = {}
    # O(n * log n)
    birds = sorted(arr)
    # O(N)
    for bird in birds:
        if bird not in birdHashMapHu.keys():
            birdHashMapHu[bird] = 1
        else:
            birdHashMapHu[bird] = birdHashMapHu[bird] + 1
    # O(N)
    return max(birdHashMapHu, key=birdHashMapHu.get)


def fromDiscussions(arr):
	count = [0]*6
	for t in arr:
		count[t] += 1

	return count.index(max(count))


def betterSolution(arr):
    # O(n * log n)
    birdSeeings = sorted(arr)

    maxBirdSeeingCount = 0  # init value
    maxBirdSeeing = 0  # init value
    currentProcessedBird = 0  # init value
    currentProcessedBirdCount = 0  # init value

    # O(N)
    for birdSeeing in birdSeeings:
        if currentProcessedBird is not birdSeeing:
            currentProcessedBird = birdSeeing
            currentProcessedBirdCount = 1
        else:
            currentProcessedBirdCount += 1
            if currentProcessedBirdCount > maxBirdSeeingCount:
                maxBirdSeeing = currentProcessedBird
                maxBirdSeeingCount = currentProcessedBirdCount

    return maxBirdSeeing


def migratoryBirds(arr):
    start = time.time()
    result = fromDiscussions(arr)
    # result = betterSolution(arr)
    end = time.time()
    print('Elapsed', end - start)
    return result


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print('Result is: ', result)
