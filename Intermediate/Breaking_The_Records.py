import math
import os
import random
import re
import sys

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

n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(result)
