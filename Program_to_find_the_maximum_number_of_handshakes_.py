n=int(input())
if n==1:
    print(n)
else:
 r=0
 i=n-1
 for i in range(0,n):
    r+=i
    i+=1
print(r)    
    