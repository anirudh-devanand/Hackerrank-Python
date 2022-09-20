import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    bid=arr[0]
    count=0
    ar={i for i in arr}
    for i in ar:
        if arr.count(i)>count:
            bid=i
        elif arr.count(i)==count:
            if i<bid:
                bid=i
        count=max(arr.count(i),count)
    return(bid)

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)
