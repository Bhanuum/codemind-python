a,b=map(int,input().split())
p=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
for i in range(0,a):
    for j in range(0,b):
        if p[i] not in c:
          if p[i]==k[j]:
            c.append(p[i])
print(len(c))            
