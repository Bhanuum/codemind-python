n=int(input())
a,b=1,2
i=0
while True:
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        a,b=b,i
        if b>n:
            p=b-n
            k=n-a
            break
    i+=1        
if p<k:
        print(p)
else:
        print(k)