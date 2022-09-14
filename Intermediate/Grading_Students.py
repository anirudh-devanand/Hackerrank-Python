import math
import os
import random
import re
import sys

def gradingStudents(grades):
    s=''
    for i in grades:
        if i<38:
            s+=str(i)+'\n'
        elif (i-(round(i//5)*5)) > 2:
            i=(round(i//5)*5)+5
            s+=str(i)+'\n'
        else:
            s+=str(i)+'\n'
    return(s)
                     

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
print(gradingStudents(grades))

