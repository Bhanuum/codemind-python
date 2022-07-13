n=int(input())
p=list(map(int,input().split()))
k=sum(p)//n
c=0
for i in p:
    if i>=k:
        c+=1
print(c)        