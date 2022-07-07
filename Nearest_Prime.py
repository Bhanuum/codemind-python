k=int(input())
for g in range(k):
 n=int(input())
 a,b=0,1
 i=2
 while True:
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        a,b=b,i
        if b>n:
            x=b-n
            v=n-a
            break
    i+=1        
 if x<v:
        print(b)
 else:
        print(a)