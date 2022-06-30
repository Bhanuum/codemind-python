def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True 
n=int(input())
k=list(map(int,input().split()))
s=0
c=0
j=[]
for i in range(0,n):
    if prime(k[i]):
        c+=1
        s+=k[i]
g=s/c        
print("%0.2f"%g)    