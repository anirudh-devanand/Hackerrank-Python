import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    x=1
    for i in range(1,n+1):
        x*=i
    print(x)

if __name__ == '__main__':
    n = int(input().strip())

extraLongFactorials(n)
