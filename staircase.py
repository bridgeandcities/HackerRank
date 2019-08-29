#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        space = n-i-1
        symbol = i+1
        for j in range(space):
            print(" ",end = "")
        for k in range(symbol):
            print("#",end = "")
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
