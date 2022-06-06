n=int(input())
p=0
i=0
while n:
    r=n%10
    p=p+r*pow(8,i)
    n=n//10
    i+=1
d=0
j=1
while p:
    r=p%2
    d=d+(r*j)
    p=p//2
    j=j*10
print(d)    