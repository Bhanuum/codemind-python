a,b=map(int,input().split())
p=list(map(int,input().split()))
k=list(map(int,input().split()))
m=set(p)
k=set(k)
c=0
for i in m:
    if i not in k:
        c+=1
for i in k:
    if i not in m:
        c+=1
print(c) 