n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(len(k)):
      c=c+k[i]
c=c//n 
for i in range(len(k)):
    if k[i]==c:
        c=1
if c==1:
    print("True")
else:
    print("False")
     