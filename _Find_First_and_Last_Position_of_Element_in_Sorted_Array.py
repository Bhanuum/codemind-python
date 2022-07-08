n=int(input())
a=list(map(int,input().split()))
t=int(input())
p=-1
k=-1
for i in range(0,n):
    if a[i]==t and k==-1:
        p=i
    if a[i]==t:
        k=i
print(p,k)    