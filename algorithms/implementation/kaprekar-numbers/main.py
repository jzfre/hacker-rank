#!/bin/python3

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def is_kaprekar(n):
    d = len(str(n))
    n_squared_str = str(n * n)
    str_len = len(n_squared_str)

    left_str = ''
    right_str = ''

    if str_len % 2 == 1:
        # take d right
        if str_len == 1:
            left_str = '0'
        else:
            left_str = n_squared_str[:d-1]

        right_str = n_squared_str[-d:]
    else:
        left_str = n_squared_str[:d]
        right_str = n_squared_str[-d:]

    return n == int(left_str) + int(right_str)


def kaprekarNumbers(p, q):
    # Write your code here

    kaprekar_numbers = []
    for i in range(p, q + 1):
        if is_kaprekar(i):
            kaprekar_numbers.append(i)

    if not len(kaprekar_numbers):
        print('INVALID RANGE')
    else:
        print(" ".join(map(str, kaprekar_numbers)))


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())

    kaprekarNumbers(p, q)
