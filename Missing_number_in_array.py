k=int(input())
for i in range(k):
    r=[]
    n=int(input())
    p=list(map(int,input().split()))
    for j in range(1,n+1):
        if j not in p:
            r.append(j)
    
    print(*r) 