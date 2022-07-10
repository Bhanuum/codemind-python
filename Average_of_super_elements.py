n=int(input())
p=list(map(int,input().split()))
k=set(p)
c=0
s=0
for i in k:
    if p.count(i)==i:
        c+=1
        s+=i
if c==0:
    print("-1")
else:
    j=s/c
    print("%0.2f" %j)
    