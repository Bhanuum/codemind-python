a,b=map(int,input().split())
c=[]
for i in range(a):
    p=list(map(int,input().split()))
    c.append(p)
for j in range(b):
    s=[]
    for i in range(a):
        s.append(c[i][j])
    print(max(s))    