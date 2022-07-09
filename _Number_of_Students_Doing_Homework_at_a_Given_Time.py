n=int(input())
l=list(map(int,input().split()))
p=int(input())
t=list(map(int,input().split()))
k=int(input())
h=0
for i in range(n):
   if t[i]>=k and k>=l[i]:
       h+=1
print(h)       