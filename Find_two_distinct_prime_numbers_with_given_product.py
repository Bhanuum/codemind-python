def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n):
    for j in range(i,n):
        if (prime(i) and prime(j)):
            if i<j:
                if i*j==n:
                    print(i,j) 
                    c=1
                    break
if c==0:
    print("-1")