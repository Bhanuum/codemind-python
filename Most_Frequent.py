n=int(input())
k=list(map(int,input().split()))
h=set(k)
c=0
ce=0
for i in h:
    p=0
    for j in range(0,n):
     if i==k[j]:
        p+=1
        if c<p:
            c=p
            ce=i
print(ce)            
            