n=int(input())
p=list(map(int,input().split()))
c=0
for i in p:
    if i==1:
        c+=1
    elif i==0:
        c+=1
if c==n:
    print(True)
else:
    print(False)