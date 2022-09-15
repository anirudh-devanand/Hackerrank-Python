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
    19: 'nineteen', 20: 'twenty', 30: 'half', 0: 'o\' clock'
    }

def timeInWords(h, m):
    if m==0:
        return(d[h]+ ' o\' clock')
    if m<=30:
        if m>20 and m<30:
            return(d[m-m%10] + ' '+ d[m%10]+' minutes past '+d[h])
        elif m==15 or m==30:
            return(d[m]+' past '+d[h])
        else:
            return(d[m]+' minutes past '+d[h])

    else:
        if h==12:
            if m>30 and m<40:
                return(d[(60-m)-((60-m)%10)] + ' '+ d[(60-m)%10]+' minutes to one')
            elif m==45:
                return(d[60-m]+' to one')
            else:
                return(d[m]+' minutes to one')

        if m>30 and m<40 and m !=45:
            return(d[(60-m)-((60-m)%10)] + ' '+ d[(60-m)%10]+' minutes to '+d[h+1])
        elif m==45:
            return(d[60-m]+' to '+d[h+1])
        else:
            return(d[60-m]+' minutes to '+d[h+1])

h = int(input().strip())

m = int(input().strip())

result = timeInWords(h, m)

print(result + '\n')