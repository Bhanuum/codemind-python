n=int(input())
p=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if p[i-1]%2==0 and p[i+1]%2!=0 or p[i-1]%2!=0 and p[i+1]%2==0:
        c+=1
print(c)   