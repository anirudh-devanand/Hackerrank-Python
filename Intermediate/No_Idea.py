import time
start_time = time.time()

n,m=input().split(' ')
s=0
arr=input().split(' ')
a=input().split(' ')    
b=input().split(' ')
for i in a:
    if i in arr and i not in b:
        s+=arr.count(i)
        arr=list(filter((i).__ne__, arr))
for i in b:
    if i in arr and i not in a:
        s-=arr.count(i)
        arr=list(filter((i).__ne__, arr))
print(s)

print("--- %s seconds ---" % (time.time() - start_time))