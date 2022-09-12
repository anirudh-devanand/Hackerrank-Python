import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr2=[i for i in arr]
    mi,ma=0,0
    arr.sort()
    arr.pop()
    arr2.sort()
    arr2.remove(arr2[0])
    for i in arr:
        mi+=i
    for i in arr2:
        ma+=i
    print(mi,ma)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
