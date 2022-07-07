n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(0,n-1):
    if p[i]<p[i+1]:
        pass
    else:
        c+=1
        break
if c==0:
    print("yes")
else:
    print("no")
  