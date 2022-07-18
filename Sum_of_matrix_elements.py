a=int(input())
b=int(input())
p=[]
for i in range(a):
    c=list(map(int,input().split()))
    p.append(c)
s=0    
for i in range(a):
    for j in range(b):
        s+=p[i][j]
print(s) 