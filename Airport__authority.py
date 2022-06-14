def amount(k):
    s=0
    for i in range(n):
        if k[i]>t:
            s+=2
        elif k[i]<=t:
           s+=1
    return s       
k=[]
n=int(input())
for i in range(n):
    j=int(input())
    k.append(j)
t=int(input())    
print(amount(k))    
    