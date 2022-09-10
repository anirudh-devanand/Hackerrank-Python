import math
import os
import random
import re
import sys

def flipMatrix(m1):
    m2 =[[0 for i in range(len(m1[0]))] for i in range(len(m1[0]))]
    m2[int(len(m1[0])/2)][int(len(m1[0])/2)]==m1[int(len(m1[0])/2)][int(len(m1[0])/2)]
    a,b=0,1
    for i in range(len(m1[0])):
        for j in range(len(m1[0])):
            if m2[a][b] != 0:
                continue
            else:
                m2[a][b]= m1[i][j]
                if b<= len(m1[0]):
                    b+=1
                else:
                    if a<3:
                         a+=1
                    else:
                        a=0
                    b=0
    return m2



def formingMagicSquare(s,iter,sum):
    if iter==7:
        return sum
    count=0
    a,b=len(s[0])/2,(len(s[0])-1)
    counter=[[a,b]]
    for i in range(1,10):
        count+= abs(s[a][b]-i)
        a+=-1
        b+=1
        if [a,b] not in counter:
            counter.append([a,b])
        else:
            a-=2
            b+=1
    sum=max(sum,count)
    iter+=1
    formingMagicSquare(flipMatrix(s),iter,sum)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s,0,0)

    fptr.write(str(result) + '\n')

    fptr.close()
