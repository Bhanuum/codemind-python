n=int(input())
k=list(map(int,input().split()))
c=0
v=0
for i in range(0,n):
    if k[i]%2==0:
        c+=1
    else:
        v+=1
print(c,v)        