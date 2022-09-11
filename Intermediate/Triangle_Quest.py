# s,r="",""
# for i in range(1,int(input())+1):
#     s+=str(i)
#     r=str(i-1)+r
#     print(s+r[:i-1])

# r,n,s=0,1,0
# for i in range(1,int(input())+1):
#     r=((i-1)*n)+r
#     s=(s*10)+i
#     print(int(((s*n*10)+(r))/10)) 
#     n*=10

for i in range(1,int(input())):
    print((10**i-1)//9*i)

