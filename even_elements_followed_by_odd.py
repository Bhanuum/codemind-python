n=int(input())
k=list(map(int,input().split()))
for i in range(n):
    if k[i]%2==0:
        print(k[i],end=" ")
for i in range(n):
    if k[i]%2!=0:
        print(k[i],end=" ")