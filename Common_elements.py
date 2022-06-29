k,l=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
p=[]
for i in range(0,k):
    for j in range(0,l):
        if n[i]==m[j]:
            if n[i] not in p:
               p.append(n[i])
print(*p)            
