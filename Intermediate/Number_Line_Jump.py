import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if x1>x2 and v1>v2:
        return('NO')
    elif x2>x1 and v2>v1:
        return('NO')
    
    if x1>x2:
        if (x1-x2)%v2==0:
            return('YES')
        else:
            return('NO')
    elif x2>x1:
        if (x1-x2)%v1==0:
            return('YES')
        else:
            return('NO')
            
first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])
v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])
result = kangaroo(x1, v1, x2, v2)

print(result)