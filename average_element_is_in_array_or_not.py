n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)//n
c=0
for i in arr:
    if s in arr:
        c+=1
if c>0:
    print(True)
else:
    print(False)