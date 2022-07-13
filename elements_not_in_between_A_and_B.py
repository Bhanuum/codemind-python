n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(0,n):
    if k[i]<a or k[i]>b:
        c.append(k[i])
if len(c)==0:
    print("-1")
else:    
  print(*c) 