n=int(input())
k=list(map(int,input().split()))
t=int(input())
c=0
for i in range(len(k)):
      if k[i]==t:
          c=1
if c==1:
    print("True")
else:
    print("False")
          
          
          