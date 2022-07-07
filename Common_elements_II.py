a,b=map(int,input().split())
p=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
for i in p:
    if i not in k:
        c.append(i)
for i in k:
    if i not in p:
        c.append(i)
print(*c)        