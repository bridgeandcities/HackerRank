#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    gradeScaled = []
    for grade in grades:
        if grade < 38:
            gradeScaled.append(grade)
        #elif grade >= 38 and grade <=40:
        #    return 40
        elif grade % 10 == 3 or grade % 10 == 4:
            gradeScaled.append((grade // 10)*10 + 5)
        elif grade % 10 == 8 or grade % 10 == 9:
            gradeScaled.append(((grade // 10)+1)*10)
        else:
            gradeScaled.append(grade)
    return gradeScaled

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
