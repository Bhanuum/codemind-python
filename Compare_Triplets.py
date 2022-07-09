n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
g=0
h=0
for i in range(len(n)):
    if n[h]>m[h]:
        c+=1
    if n[h]<m[h]:
        g+=1
    if n[h]==m[h]:
        pass
    h+=1
print(c,g)  