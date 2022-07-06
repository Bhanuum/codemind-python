def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
m=int(input())
rev=0
n=m
while n:
    r=n%10
    rev=rev*10+r
    n//=10
if prime(m) and prime(rev):
    print("circular prime")
elif prime(m) or prime(rev):
    print("prime but not a circular prime")
else:
    print("not prime")
