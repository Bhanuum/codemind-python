n=int(input())
k=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    if k[i]%2==0:
        c+=k[i]
    else:
        s+=k[i]
k=c-s
if k<0:
    k=k*-1
print(k)        