def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
p=list(map(int,input().split()))
m=p.index(min(p))
n=p.index(max(p))
c=0
if m<n:
    for i in range(m,n+1):
        if prime(p[i]):
          c+=1
    print(c)     
else:
    for i in range(n,m+1):
        if prime(p[i]):
            c+=1
    print(c)