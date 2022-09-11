import math
import os
import random
import re
import sys

def time_delta(t1, t2):
    
    sign1=t1.split(' ')[-1][0]
    sign2=t2.split(' ')[-1][0]
    t1diff=int(t1.split(' ')[-1])
    t2diff=int(t2.split(' ')[-1])
    absdiff=t1diff+t2diff
    if sign1 != sign2:
        absdiff-=2400
    absdiff=(int(absdiff%100)*60)+int((absdiff//100)*3600)
    print(absdiff)
    t1=t1.split(' ')[-2]
    t2=t2.split(' ')[-2]
    abst1=(int(t1.split(':')[0])*3600)+(int(t1.split(':')[1])*60)+(int(t1.split(':')[2]))
    abst2=(int(t2.split(':')[0])*3600)+(int(t2.split(':')[1])*60)+(int(t2.split(':')[2]))
    return(str(abs((abst1-abst2)+abs(absdiff))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
