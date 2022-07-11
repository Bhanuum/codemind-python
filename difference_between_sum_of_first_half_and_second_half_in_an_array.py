n=int(input())
p=list(map(int,input().split()))
k=n//2
g=0
h=0
for i in range(0,k):
    g+=p[i]
for i in range(k,n):
    h+=p[i]
k=g-h
if k<0:
    k*=-1
print(k)    