def add(n):
    if n<0:
        n=n*-1
    return len(str(n))
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    p=add(i)
    k.append(p)
j=max(k)   
for i in l:
    if add(i)==j:
        print(i,end=" ")
        