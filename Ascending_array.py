n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(0,n-1):
    if k[i]<k[i+1]:
        c+=1
if c==n-1:
    print("yes")
else:
    print("no")