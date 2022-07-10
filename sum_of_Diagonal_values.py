m,n=map(int,input().split())
p=[]
for i in range(n):
    h=list(map(int,input().split()))
    p.append(h)
s=0
for i in range (n):
    for j in range (m):
        if i==j or i+j==n-1:
            s+=p[i][j]
print(s)            