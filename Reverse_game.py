n=int(input())
k=list(map(int,input().split()))
for i in range(0,n):
    n=k[i]
    rev=0
    while n:
      r=n%10
      rev=rev*10+r
      n//=10
    print(rev,end=" ") 