n=int(input())
p=[]
for i in range(1,n+1):
    r=n%i
    if r==0:
        if i==1:
            p.append(i)
        else:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                  p.append(i)
                  break
print(len(p))                
            
        