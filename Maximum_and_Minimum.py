n=int(input())
l=list(map(int,input().split()))
p=[]
k=set(l)
c=0
for i in k:
    if l.count(i)==i:
        p.append(i)
        c+=1
if c==0:
    print("-1")
else:
  h=min(p)
  g=max(p)
  print(h,g,end=" ")
