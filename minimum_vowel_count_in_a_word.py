p=input()
s=p.split()
u=[]
for i in s:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    u.append(c)

for i in range(0,len(u)):
    min=u[0]
    if u[i]<min:
        min=u[i]
print(min)
