import math
import os
import random
import re
import sys

def formingMagicSquare(s):
    sum=0
    a,b=len(s[0])/2,(len(s[0])-1)
    counter=[[a,b]]
    for i in range(1,10):
        sum+= abs(s[a][b]-i)
        a+=-1
        b+=1
        if [a,b] not in counter:
            counter.append([a,b])
        else:
            a-=2
            b+=1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
