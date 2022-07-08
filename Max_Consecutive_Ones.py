n=int(input())
k=list(map(int,input().split()))
c=0
p=0
for i in range(0,n):
    if k[i]==1:
        c+=1
    if k[i]==0:
       if p<c:
           p=c
       c=0
if c>p:
    p=c
print(p)    