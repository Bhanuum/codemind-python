n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    p.append(i)
if n%2!=0:
    p.append("0")
print(*p)    