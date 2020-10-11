#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#


def getMoneySpent(keyboards, drives, maxToSpend):
    #
    # Write your code here.
    #
    keyboards.sort()
    drives.sort()

    print(f'Keyboars {keyboards}')
    print(f'Drivers {drives}')
    print(f'b {maxToSpend}')

    result = -1

    for keyboard in keyboards[::-1]:
        print(f'Current kebyard: ', keyboard)
        if keyboard > maxToSpend:
            print('Keyboard more than max')
            continue
        for drive in drives[::-1]:
            print(f'Current drive:', drive)

            if drive > maxToSpend:
                print('Drive more than max')
                continue

            currentDriveAndKeyboard = drive + keyboard

            if currentDriveAndKeyboard > maxToSpend:
                print('Overflowed price')
                continue

            elif currentDriveAndKeyboard == maxToSpend:
                print('Max applied')
                return maxToSpend

            elif currentDriveAndKeyboard < maxToSpend:
                if (currentDriveAndKeyboard > result):
                    result = drive + keyboard

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
