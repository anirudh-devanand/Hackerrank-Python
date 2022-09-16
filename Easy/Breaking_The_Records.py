#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    mini=scores[0]
    maxi=scores[0]
    mi=0
    ma=0
    for i in range(1,len(scores)):
        if scores[i]>maxi:
            maxi=scores[i]
            ma+=1
        if scores[i]<mini:
            mini=scores[i]
            mi+=1
    return([ma,mi])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
