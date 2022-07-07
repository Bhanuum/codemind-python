n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(0,n-1):
    if p[i]>p[i+1]:
        c+=1
if c+1==n:
    print("yes")
else:
    print("no")