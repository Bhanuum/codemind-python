n=int(input())
p=n%10
n//=10
u=n%10
n//=10
j=n%10
n//=10
k=n%10
n//=10
if k==6:
    k=9
elif j==6:
    j=9
elif u==6:
    u=9
else:
    p=9
print(k,j,u,p,sep="")     