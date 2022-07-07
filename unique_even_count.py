n=int(input())
p=list(map(int,input().split()))
c=[]
for i in range(0,n):
   if p[i]%2==0:
       if p[i] not in c:
           c.append(p[i])
print(len(c))           