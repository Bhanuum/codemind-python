m,n=map(int,input().split())
p=[]
s=0
for i in range(m):
    h=list(map(int,input().split()))
    p.append(h)
for j in range (n):
    for i in range(m):
        s+=p[i][j]
print(s)        