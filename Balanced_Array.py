n=int(input())
for i in range(n):
    t=int(input())
    p=list(map(int,input().split()))
    c=0
    for i in range(0,t):
        if sum(p[:i])==sum(p[i+1:]):
            c+=1
    if c==0:
        print("NO")
    else:
        print("YES")