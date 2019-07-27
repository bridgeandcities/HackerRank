#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    print(a)
    #print(b)
    count = 0
    lcm = b[0]
    gcd = a[-1]
    possible = []
    ans = []
    for i in range(gcd, lcm+1):
            if all(i % x == 0 for x in a) == True:
                possible.append(i)
    #print("possible: ", possible)
    for j in possible:
        if (all(y % j == 0 for y in b)) == True:
            ans.append (j)
            
    #print("ans: ", ans)
    return len(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
