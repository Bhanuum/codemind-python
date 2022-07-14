n=int(input())
k=list(map(int,input().split()))
l=min(k)
c=0
for i in k:
 g=str(i)
 if len(g)==len(str(l)):
     c+=1
print(c)     