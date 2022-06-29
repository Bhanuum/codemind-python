n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(0,n):
    c+=p[i]
print(c)    