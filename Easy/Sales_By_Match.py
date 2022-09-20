import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    pair=0
    ar.sort()
    arr={i for i in ar}
    print(arr)
    for i in arr:
        pair+=(ar.count(i))//2
    return(pair)

    
n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)