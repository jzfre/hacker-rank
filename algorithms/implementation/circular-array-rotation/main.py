#!/bin/python3

import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

# Python code to implement the above approach
def right_rotation(a, k):
   # if the size of k > len(a), rotate only necessary with
   # module of the division
   rotations = k % len(a)
   return a[-rotations:] + a[:-rotations]
 

def circularArrayRotation(a, k, queries):
    # a - array, k - num of rotations, queries array of indexes
    res = []
    rotated = right_rotation(a, k)
    for e in queries:
      res.append(rotated[e])
    
    return res

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
