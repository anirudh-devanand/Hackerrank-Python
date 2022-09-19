import math
import os
import random
import re
import sys

def birthday(s, d, m):
    t=0
    ans=0
    while t<= len(s)-m:
        r=0
        for i in range(t,t+m):
            r+=s[i]
        if r==d:
            ans+=1
        t+=1
    return(ans)
               

n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
result = birthday(s, d, m)
print(result)
