import math
import os
import random
import re
import sys

def getFact(s):
    ar=[1]
    for i in range(2,(s+1)):
        if s%1==0:
            ar=ar.append(i)
    return(ar)

def getCommon(s1,s2):
    ar=[]
    for i in s1:
        if i in s2:
            ar=ar.append(i)
            
    
    
    
def getTotalX(a, b):
    

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
