a=int(input())
k=list(map(int,input().split()))
b=int(input())
c=0
for i in set(k):
    if k.count(i)==b:
        print(i,end=" ")
        c+=1
if c==0:
    print("-1")
        