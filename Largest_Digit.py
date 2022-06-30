n=int(input())
b=0
while n:
    r=n%10
    n//=10
    if b<r:
        b=r
print(b)        