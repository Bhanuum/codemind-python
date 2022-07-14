n=input().lower()
p=n.split()
k=p[0]
c=0
for i in k:
    s=0
    for j in range(1,len(p)):
        if i in  p[j]:
            s+=1
    if s==len(p)-1:
        c+=1
print(c) 