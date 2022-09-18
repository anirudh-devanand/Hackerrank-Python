import math
import os
import random
import re
import sys

def getFact(s):
    arr=[]
    for j in s:
        ar=[1]
        for i in range(2,j+1):
            if j%i==0:
                ar.append(i)
        arr.append(ar)
    return(arr)

    
def getCommon(s):
    for i in range (len(s)-1):
        ar=[]
        for j in s[i]:
            if j in s[i+1]:
                ar.append(j)
        s[i+1]=ar
    return(s[-1])
            
    
def getTotalX(a, b):
    ans=0
    facts=getFact(getCommon(getFact(b)))
    for i in facts:
        s=0
        for j in a:
            if j in i:
                s+=1
        if s==len(a):
            ans+=1      
    return(ans)
    
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)

print(total)