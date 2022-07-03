n=input()
m=input()
n=n.lower()
m=m.lower()
g=[]
for i in n:
    for j in m:
        if i in j and i!=" ":
            if i not in g:
              g.append(i)
print(len(g))