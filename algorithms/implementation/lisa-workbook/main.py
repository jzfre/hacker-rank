#!/bin/python3

import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#
def workbook(n, k, arr):
    total = 0
    
    current_page = 1

    for i in range(1, n + 1):
        
        min = None
        max = None

        per_chapter = arr[i-1]
        pages_per_chapter = per_chapter // k
        if (per_chapter % k != 0):
            pages_per_chapter += 1    
        
    
        # iterate over pages
        for j in range(1, pages_per_chapter + 1):
            min = 1 + k * (j - 1)
            if (k * j > per_chapter):
                max = per_chapter % k + (k * (j - 1))
            else:
                max = k * j

            if current_page >= min and current_page <= max:
                total += 1

            current_page += 1

    return total


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
