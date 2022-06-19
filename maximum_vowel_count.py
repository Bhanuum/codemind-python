p=input()
s=p.split()
u=[]
for i in s:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    u.append(c)
v=0
for i in range(1,len(u)):
    if u[i]>v:
        v=u[i]
print(v)
