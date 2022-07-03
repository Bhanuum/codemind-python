n=int(input())
a,b=0,1
i=0
while True:
   for j in range(2,int(i**0.5)+1):
       if i%j==0:
           break
   else:
       a=b
       b=i
       if b>n:
        l=b-n
        r=n-a
        break
   i+=1
if l<r:
    print(l)
else:
    print(r)
 