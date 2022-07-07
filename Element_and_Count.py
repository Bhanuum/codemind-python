n=int(input())
p=list(input())
c=[]
for i in p:
    if i!=" ":
        if i not in c:
          c.append(i)
          c.append(p.count(i))
print(*c)    