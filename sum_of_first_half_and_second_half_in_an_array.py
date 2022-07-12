n=int(input())
l=list(map(int,input().split()))
b=n//2
s=0
p=0
for i in range(0,b):
    s+=l[i]
for i in range(b,n):
    p+=l[i]
print(s)
print(p)
