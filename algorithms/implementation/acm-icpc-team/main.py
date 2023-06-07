#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    for idx, bn in enumerate(topic):
        num = int(bn, 2)
        print(idx, num)
    # 1 1 1 1 1  -> 1 + 2 + 4 + 8 + 16 -> 0 - 31 => 32 kombinacii 
    # 11000 - 24
    # 00111 - 7



if __name__ == '__main__':
    topic = ['10101', '11110', '00010']

    result = acmTeam(topic)
    print(result)
