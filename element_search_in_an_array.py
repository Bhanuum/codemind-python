n= int(input())
arr = list(map(int,input().split()))
b=int(input())
c=0
for i in arr:
    if b in arr:
        c+=1
if c>0:
    print(True)
else:
    print(False)