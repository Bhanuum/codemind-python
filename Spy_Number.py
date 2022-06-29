n=int(input())
p=n
c=0
s=1
while p:
    r=p%10
    p//=10
    c+=r
    s*=r
if s==c:
    print("Spy Number")
else:
    print("Not Spy Number")