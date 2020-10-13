#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def isDivisibleBy(num, by):
    return not bool(num % by)

def isOverleapJulian(year):
    return isDivisibleBy(year, 4)

def isOverleapGregorian(year):
    return ((isDivisibleBy(year, 400)) or (isDivisibleBy(year, 4) and (not isDivisibleBy(year, 100))))

# print 256th day of the year
def dayOfProgrammer(year):
    if year < 1918:  # Julian calendar
        if isOverleapJulian(year):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    elif year > 1918:  # Gregorian calendar
        if isOverleapGregorian(year):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    else:  # special case
        return '26.09.1918'


if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print('Result: ', result)
