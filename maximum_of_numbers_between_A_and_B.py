n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
p=[]
h=0
for i in range(0,n):
    if k[i]>=a and k[i]<=b:
        h+=1
        p.append(k[i])
if h>0:
    print(max(p))
elif h==0:
    print("-1")