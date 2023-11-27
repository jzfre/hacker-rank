#!/bin/python3

import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    total = 0
    games_count = 0
    current_price = p
    while True:
        # print('T', total, 'GC', games_count, 'CP', current_price)

        if s < current_price + total:
            return games_count

        total = total + current_price
        games_count = games_count + 1

        # make a sale for next buy
        if (current_price - d >= m):
            current_price = current_price - d
        else:
            current_price = m


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
