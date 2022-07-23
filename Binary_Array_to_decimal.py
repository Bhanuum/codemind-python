n=int(input())
p=list(map(int,input().split()))
r=0
g=0
for i in range(n-1,-1,-1):
    r=r+p[i]*(2**g)
    g+=1
print(r)    
    
    