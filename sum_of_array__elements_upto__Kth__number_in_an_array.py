n=int(input())
p=list(map(int,input().split()))
a=int(input())
c=0
for i in range(0,n):
    if p[i]==a:
        c+=p[i]
        break
    else:
        c+=p[i]
print(c)    