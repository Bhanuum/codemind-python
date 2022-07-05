n=input().lower()
m=n.split()
c=0
for i in m:
    p=i[::-1]
    if i==p:
        c+=1
print(c)        