n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)//n
c=0
for i in arr:
    if i<=s:
       c+=1
print(c) 