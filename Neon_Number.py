n=int(input())
p=n*n
c=0
while p:
    r=p%10
    p//=10
    c+=r
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")
