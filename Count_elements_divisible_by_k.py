a,b=map(int,input().split())
p=list(map(int,input().split()))
c=0
for i in range(0,a):
    if p[i]%b==0:
        c+=1
print(c)        