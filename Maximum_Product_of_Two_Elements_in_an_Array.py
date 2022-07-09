n=list(map(int,input().split()))
p=0
for i in range(0,len(n)):
    for j in range(0,len(n)):
        v=(n[i]-1)*(n[j]-1)
        if v>p and i!=j:
            p=v
print(p)   