a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(a):
    if l[i]<0:
        l[i]=abs(l[i])
p=[]
c=0
for i in l:
    k=str(i)
    j=len(k)
    k=int(j)
    p.append(k)
for i in p:
    if i==b:
        c+=1
print(c)        