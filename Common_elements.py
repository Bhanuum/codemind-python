a,b=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
g=[]
for i in range(0,a):
    for j in range(0,b):
        if p[i]==q[j]:
            if p[i] not in g:
               g.append(p[i])
print(*g) 
