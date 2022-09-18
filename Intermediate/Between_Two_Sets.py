import math
import os
import random
import re
import sys

def getFact(s):
    arr=[]
    for j in s:
        ar=[1]
        for i in range(2,(s+1)):
            if s%1==0:
                ar=ar.append(i)
        arr=arr.append(ar)
    return(ar)

    
def getCommon(s):
    for i in range (len(s)-1):
        ar=[]
        for j in s[i]:
            if j in s[i+1]:
                ar=ar.append(j)
        s[i+1]=ar
    return(s[-1])
            
    
def getTotalX(a, b):
    ans=0
    facts=getFact(getCommon(getFact(b)))
    for i in facts:
        if i in a:
            ans+=1       
    return(ans)
    

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
