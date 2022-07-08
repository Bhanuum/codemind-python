n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    j=list(map(int,input().split()))
    k=list(map(int,input().split()))
    c=[]
    for h in j:
        if i!=" ":
            c.append(h)
    for f in k:
        if i!=" ":
            c.append(f)
    print(*sorted(c))        
