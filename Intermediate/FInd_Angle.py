import math
a=int(input())
b=int(input())
c=(math.sqrt(a**2 + b**2))
d=math.sqrt(c**2-b**2)
tanx=d/b
x=((str(math.degrees(math.atan(tanx)))).split('.'))[0]
print(x)

