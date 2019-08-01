#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    ans = [0]*5
    for bird in arr:
        if bird == 1:
            ans[0] += 1
        elif bird == 2:
            ans[1] += 1
        elif bird == 3:
            ans[2] += 1
        elif bird == 4:
            ans[3] += 1
        else:
            ans[4] += 1
    return ans.index(max(ans))+1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
