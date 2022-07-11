def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(1,10000):
    p=n+i
    h=str(p)
    k=h[::-1]
    if int(k)==p:
        if prime(p):
            print(p)
            break