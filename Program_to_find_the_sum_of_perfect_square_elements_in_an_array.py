n=int(input())
p=list(map(int,input().split()))
import math
s=0
for i in p:
    k=int(math.sqrt(i))
    if k*k==i:
        s+=i
print(s)  