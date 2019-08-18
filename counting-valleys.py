#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    reset = False
    valleys = 0
    for letter in s:
        if letter == "D":
            count -= 1
        else:
            count += 1
        if count < 0 and reset == False:
            valleys += 1
            reset = True
        elif count == 0 and reset == True:
            reset = False
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
