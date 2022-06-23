n=int(input())
k=list(map(int,input().split()))
p=[]
for i in k:
    if i not in p:
       if k.count(i)!=1:
           p.append(i)
print(*p)           
       