n=int(input())
p=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(0,n):
    if p[i]>=a and p[i]<=b:
        c.append(p[i])
if len(c)>1:        
 print(max(c))  
else:
    print("-1")