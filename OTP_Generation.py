n=input()
p=""
for i in n:
    k=int(i)
    if k%2!=0:
        j=k*k
        p+=str(j)
print(p) 