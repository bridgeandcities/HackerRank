#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleDist = []
    orangeDist = []
    for apple in apples:
        appleDist.append(apple+a)
    for orange in oranges:
        orangeDist.append(orange+b)
    appleCount = 0
    orangeCount = 0
    for i in appleDist:
        if i <= t and i >= s:
            appleCount +=1
    for j in orangeDist:
        if j <=t and j >= s:
            orangeCount +=1
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
