n=int(input())
m=int(input())
for i in range(n,m+1):
  c=0
  k=0
  p=i
  while p:
    r=p%10
    p//=10
    c+=1
    if r==0:
        break
    if i%r==0:
        k+=1
  if k==c:
    print(i,end=" ")
    