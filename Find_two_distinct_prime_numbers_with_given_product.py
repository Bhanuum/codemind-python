def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    return n
n=int(input())
f=0
for i in range(1,n):
    for j in range(i,n):
        if (prime(i) and prime(j)):
            if i<j and i*j==n:
                print(i,j)
                f+=1
                break
if f==0:
    print("-1")
        