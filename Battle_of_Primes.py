def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True 
n=int(input())
m=int(input())
k=n+m
for i in range(1,100):
    if prime(i+k):
        print(i)
        break