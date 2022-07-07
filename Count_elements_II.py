a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
p=set(m)
k=set(n)
c=[]
for i in p:
    if i not in k:
        c.append(i)
for i in k:
    if i not in p:
        c.append(i)
print(len(c))    