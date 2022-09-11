import math
a=int(input())
b=int(input())
c=(math.sqrt(a**2 + b**2))
d=math.sqrt(c**2-b**2)
tanx=d/b
x=round((math.degrees(math.atan(tanx))))
degree_sign = u'\N{DEGREE SIGN}'
print(x,degree_sign,sep='')

