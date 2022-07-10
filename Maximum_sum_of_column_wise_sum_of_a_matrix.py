m,n=map(int,input().split())
p=[]
x=0
for i in range(m):
    h=list(map(int,input().split()))
    p.append(h)
for j in range (n):
    s=0
    for i in range(m):
        s+=p[i][j]
    if x<s:
        x=s
print(x) 