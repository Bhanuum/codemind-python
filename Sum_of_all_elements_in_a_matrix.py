n,m=map(int,input().split())
b=[]
for i in range(n):
    p=list(map(int,input().split()))
    b.append(p)
s=0
for i in range(n):
    for j in range(m):
        s+=b[i][j]
print(s)        