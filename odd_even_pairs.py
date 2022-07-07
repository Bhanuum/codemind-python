n=int(input())
p=list(map(int,input().split()))
v=[]
c=[]
for i in range(0,n):
     if p[i]%2==0:
        c.append(p[i])
     if p[i]%2!=0:
        v.append(p[i])
i=0
j=0
while i<len(v) or j<len(c):
    if i<len(v):
        print(v[i],end=" ")
        i+=1
    if j<len(c):
        print(c[j],end=" ")
        j+=1
if n%2!=0:
    print("0",end=" ")