import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    ans=0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i]+ar[j])%k==0:
                ans+=1
                
    return(ans)
                
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)