import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    bid=arr[0]
    count=0
    for i in arr:
        if arr.count(i)==count:
            if i<bid:
                bid=i
        elif arr.count(i)>count:
            bid=i
        count=max(arr.count(i),count)
    return(bid)

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)
