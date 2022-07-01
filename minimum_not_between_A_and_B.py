n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
p=[]
h=0
for i in range(0,n):
    if k[i]>=a and k[i]<=b:
        p.append(k[i])
f=[]        
for i in k:
    if i not in p:
        h+=1
        f.append(i)
if h>0:        
 print(min(f))   
else:
    print("-1")