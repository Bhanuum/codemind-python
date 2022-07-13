n=int(input())
p=list(map(int,input().split()))
c=0
k=[]
for i in range(n):
    if p[i]%2!=0:
        k.append(p[i])
for i in range(0,n):
   if p[i]%2!=0:
        if i%2!=0:
          c+=1
if len(k)==c:
    print(True)
else:
    print(False)
   