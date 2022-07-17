n=input()
i=0
b=0
c=0
p=len(n)
for i in range(p):
    if n[i]=="R":
        c+=1
    else:
        c-=1
    i+=1    
    if c==0:
        b+=1
    p-=1
print(b)    