n=int(input())
a,b=0,1
i=0
while True:
    c=2**i
    a=b
    b=c
    if b>n:
        l=b-n
        r=n-a
        break
    i+=1
if l<r:
    print(l)
else:
    print(r)
 