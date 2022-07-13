n=input().lower()
p=" "
for i in n:
    if i not in p:
        p+=i
k=list(p)
j=(sorted(k))
g=""
for i in j:
    if i!=" ":
     g+=str(i)
print(g)    