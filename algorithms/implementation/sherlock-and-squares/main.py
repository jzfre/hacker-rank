#!/bin/python3
import math

def squares(a, b):
    return math.floor(math.sqrt(b)) + 1 - math.ceil(math.sqrt(a))
      
if __name__ == '__main__':
    print(len([i for i in range(5, 8)]))

