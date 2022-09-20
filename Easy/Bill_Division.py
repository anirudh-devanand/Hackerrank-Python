import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    a=bill.pop(k)
    if sum(bill)/2==b:
        print('Bon Appetit')
    else:
        print(int(a/2))

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b= int(input().strip())

bonAppetit(bill, k, b)
