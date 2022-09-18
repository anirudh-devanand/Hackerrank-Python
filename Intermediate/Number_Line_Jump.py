#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1>x2 and v1>v2:
        return('NO')
    elif x2>x1 and v2>v1:
        return('NO')
    
    if x1>x2:
        if (x1-x2)%v1==0:
            return('YES')
        else:
            return('NO')
    elif x2>x1:
        if (x1-x2)%v2==0:
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