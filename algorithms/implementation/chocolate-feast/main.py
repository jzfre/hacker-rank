#!/bin/python3
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # lets check how many bars he can buy
    total_eaten_bars = n // c
    
    if (total_eaten_bars < m):
        return total_eaten_bars

    wrapper_stack = total_eaten_bars

    while (True):
      eaten_bars = wrapper_stack // m
      if (eaten_bars <= 0):
        return total_eaten_bars

      total_eaten_bars += eaten_bars
      wrapper_stack = eaten_bars + (wrapper_stack % m)

    
if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
