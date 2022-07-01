n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(0,n):
    if k[i]>=a and k[i]<=b:
        c+=k[i]
print(c)        
