#!/bin/python3

import math
import os
import random
import re
import sys

numWords = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fiveteen',
    'sixteen',
    'seventeen',
    'eightteen',
    'nineteen',
    'twenty',
    'twenty one',
    'twenty two',
    'twenty three',
    'twenty four',
    'twenty five',
    'twenty six',
    'twenty seven',
    'twenty eight',
    'twenty nine'
]

# Complete the timeInWords function below.


def timeInWords(h, m):
    # resolute minutes

    # if 00 then return
    if m == 0:
        return numWords[h - 1] + ' o\' clock'

    if m < 30:
        if m == 1:
            return 'one minute past ' + numWords[h - 1]
        elif m == 15:
            return 'quarter past ' + numWords[h - 1]
        else:
            return numWords[m - 1] + ' minutes past ' + numWords[h - 1]
    elif m == 30:
        return 'half past ' + numWords[h - 1]
    else:
        if m == 45:
            return 'quarter to ' + numWords[h]
        elif m == 59:
            return 'one minute to ' + numWords[h]
        else:
            return numWords[60 - m - 1] + ' minutes to ' + numWords[h]


if __name__ == '__main__':
    h = int('05')
    m = int('50')

    result = timeInWords(h, m)
    print(result)
