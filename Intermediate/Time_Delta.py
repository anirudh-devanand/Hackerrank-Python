import math
import os
import random
import re
import sys
from datetime import datetime


def time_delta(t1, t2):
    months = {
   'Jan':'01',
   'Feb':'02',
   'Mar':'03',
   'Apr':'04',
   'May':'05',
   'Jun':'06',
   'Jul':'07',
   'Aug':'08',
   'Sep':'09',
   'Oct':'10',
   'Nov':'11',
   'Dec':'12'
    }
    t1=t1.replace(t1[7:10], months[t1.split(' ')[2]])
    t2=t2.replace(t2[7:10], months[t2.split(' ')[2]])
    if ':' in str(datetime.strptime(t1[4:14], "%d %m %Y")-datetime.strptime(t2[4:14], "%d %m %Y")).split(' ')[0]:
        delta=0
    else:
        delta=(int(str((datetime.strptime(t1[4:14], "%d %m %Y")-datetime.strptime(t2[4:14], "%d %m %Y"))).split(' ')[0])-1)*86400
    sign1=t1.split(' ')[-1][0]
    sign2=t2.split(' ')[-1][0]
    t1diff=int(t1.split(' ')[-1])
    t2diff=int(t2.split(' ')[-1])
    absdiff=t1diff+t2diff
    if sign1 != sign2:
        absdiff-=2400
    absdiff=(int(absdiff%100)*60)+int((absdiff//100)*3600)
    t1=t1.split(' ')[-2]
    t2=t2.split(' ')[-2]
    abst1=(int(t1.split(':')[0])*3600)+(int(t1.split(':')[1])*60)+(int(t1.split(':')[2]))
    abst2=(int(t2.split(':')[0])*3600)+(int(t2.split(':')[1])*60)+(int(t2.split(':')[2]))
    return(str(abs((abst1-abst2)+abs(absdiff)+abs(delta))))



t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)

    print(delta + '\n')
