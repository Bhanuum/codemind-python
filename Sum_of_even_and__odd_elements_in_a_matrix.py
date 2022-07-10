n,m=map(int,input().split())
b=[]
for i in range(n):
    p=list(map(int,input().split()))
    b.append(p)
s=0
v=0
for i in range(n):
    for j in range(m):
       if b[i][j]%2==0:
           s+=b[i][j]
       else:
            v+=b[i][j]
print(s,v)            