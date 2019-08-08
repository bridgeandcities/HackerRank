#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    #print(scores)
    high = scores[0]
    low = scores[0]
    win = 0
    loss = 0
    for i in scores[1:]:
        if i > high:
            win += 1
            high = i
        elif i < low:
            loss += 1
            low = i
    return [win, loss]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
