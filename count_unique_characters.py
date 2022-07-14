n=input().lower()
p=0
for i in n:
    if n.count(i)==1 and i!=" ":
        p+=1
print(p)