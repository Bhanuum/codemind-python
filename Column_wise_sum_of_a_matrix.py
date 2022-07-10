n,m=map(int,input().split())
b=[]
for i in range(n):
    p=list(map(int,input().split()))
    b.append(p)
v=0
for j in range(m):
    s=0
    for i in range(n):
        s+=b[i][j]
    print(s,end=" ")
    s=0
    