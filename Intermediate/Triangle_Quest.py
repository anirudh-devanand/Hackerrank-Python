s,r="",""
for i in range(1,int(input())+1):
    s+=str(i)
    r=str(i-1)+r
    print(s+r[:i-1])
