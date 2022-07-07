n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(0,n):
    if p[i]%2==0:
        break
    else:
        c+=p[i]
print(c)    