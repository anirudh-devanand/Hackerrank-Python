import math
import os
import random
import re
import sys

def plusMinus(arr):
    p,n,z=0.000000,0.000000,0.000000
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
    print("{}\n{}\n{}".format(round(p/len(arr),6),round(n/len(arr),6),round(abs((p+n)-len(arr))/len(arr),6)))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)