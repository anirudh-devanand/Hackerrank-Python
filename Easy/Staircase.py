#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    s=''
    for i in range(n):
        s+=' '
    for i in range(n):
        s=s.replace(s[i],'#',1)
        print(s[::-1])

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)