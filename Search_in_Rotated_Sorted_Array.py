n=int(input())
k=list(map(int,input().split()))
b=int(input())
c=0
for i in range(0,n):
    if k[i]==b:
        c=i
if c==0:
    print("-1")
else:
    print(c)