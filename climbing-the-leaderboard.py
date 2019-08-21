#!/bin/python3
/*
This code fails test case 6 to 9 due to timeout error. Needs optimization (perhaps by implementing binary search)
but is correct given enough time to run.
*/
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    #print(alice)
    scores = sorted(list(set(scores)), reverse=True)
    #print(scores)
    lenScores = len(scores)
    result = []
    for aliceScore in alice:
        #print("alice's score: ", aliceScore)
        for i in range(len(scores)):
            #print("place: ", i+1, "Score: ", scores[i], lenScores)
            if aliceScore >= scores[i]:
                #print(i+1)
                result.append(i+1)
                break
            if i+1 == lenScores:
                #print(i+2)
                result.append(i+2)
                break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
