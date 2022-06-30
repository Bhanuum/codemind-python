def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
p=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    if prime(p[i]):
        c+=1
        s+=p[i]
k=s/c
print("%0.2f" %k)