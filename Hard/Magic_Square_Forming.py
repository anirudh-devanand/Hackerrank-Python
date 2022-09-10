import math
import os
import random
import re
import sys

def flipMatrix(m1,iter):
    if iter<=4:
        j=0
    else:
        j=1
    temp = m1[0][j]
    m1[0][j] = m1[2- j][0]
    m1[2 - j][0] = m1[2][2 - j]
    m1[2][2 - j] = m1[j][2]
    m1[j][2] = temp
    return m1

def formingMagicSquare(s,iter,sum):
    if iter==7:
        print (sum)
        return
    count=0
    a=int(len(s[0])/2)
    b=int(len(s[0])-1)
    counter=[[a,b]]
    for i in range(1,10):
        count+= abs(s[a][b]-i)
        a+=-1
        b+=1
        if a>2:
            a=0
        elif a<0:
            a=2
        if b>2:
            b=0
        if [a,b] not in counter:
            counter.append([a,b])
        else:
            a-=2
            b+=1
            if a>2:
                a=0
            elif a<0:
                a=2
            if b>2:
                b=0
    sum=min(sum,count)
    iter+=1
    formingMagicSquare(flipMatrix(s,iter),iter,sum)
    
    

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = [[5,3,4],[1,5,8],[6,4,2]]

#    for _ in range(3):
#        s.append(list(map(int, input().rstrip().split())))

formingMagicSquare(s,0,math.inf)


#    fptr.write(str(result) + '\n')

#    fptr.close()
