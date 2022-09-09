import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1,d2=0,0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j==i:
                d1+=arr[i][j]
            if j+i==(len(arr[i])-1):
                d2+=arr[i][j]
    print (d2)
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()