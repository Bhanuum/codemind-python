n=input().split()
for i in n:
    k=ord(min(i))-ord(max(i))
    if k<=0:
        k=k*-1
        print(k,end=" ")