n=int(input())
k=list(map(int,input().split()))
s=""
for i in range(n):
    s+=str(k[i])
p=int(s)+1
p=str(p)
for i in p:
    print(i,end=" ")
