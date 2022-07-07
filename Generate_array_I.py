n=int(input())
k=list(map(int,input().split()))
p=[]
for i in range(0,n,2):
    j=0
    while j<k[i+1]:
        p.append(k[i])
        j+=1
print(*p)        