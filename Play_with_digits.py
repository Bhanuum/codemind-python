n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=0
    while p[i]:
        r=p[i]%10
        p[i]//=10
        s+=r
    c+=s
print(c) 