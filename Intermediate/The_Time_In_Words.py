import math
import os
import random
import re
import sys

d = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'half', 0: 'o\'clock'
    }

def timeInWords(h, m):
    if m<=30:
        if m>20 and m<30:
            print(d[m-m%10] + ' '+ d[m%10]+'minutes past '+d[h])
        else:
            print(d[m]+'minutes past '+d(h))
    else:
        if h==12:
            if m>40 and m<60:
                print(d[(60-m)-((60-m)%10)] + ' '+ d[(60-m)%10]+'minutes to one')
            else:
                print(d[60-m]+'minutes to one')
        if m>40 and m<60:
            print(d[(60-m)-((60-m)%10)] + ' '+ d[(60-m)%10]+'minutes to '+[h+1])
        else:
            print(d[60-m]+'minutes to '+d[h+1])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
