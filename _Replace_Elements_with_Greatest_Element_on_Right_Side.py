n=int(input())
k=list(map(int,input().split()))
c=[]
for i in range(0,n):
    h=0
    p=max(k)
    c.append(p)
    k.remove(k[h])
    h+=1
c.remove(c[0])
for i in range(len(c)):
    print(c[i],end=" ")
print("-1")    