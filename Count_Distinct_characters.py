n=input().lower()
p=[]
for i in n:
    if i not in p and i!=" ":
        p.append(i)
print(len(p))