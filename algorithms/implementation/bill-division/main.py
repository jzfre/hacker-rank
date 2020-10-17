#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    # how the fuck is this handled is it copy or reference?
    correctBil = bill
    # make the bill to have values only that the bitch ate
    del correctBil[k]
    # make a sum of bullshit they eat together
    bActual = int(sum(correctBil) / 2)
    diff = b - bActual
    if diff is not 0:
        print(diff)
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
