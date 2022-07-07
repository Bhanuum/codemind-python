n=input().lower()
m=input().lower()
c=[]
for i in n:
    if i not in m and i!=" ":
        if i not in c:
            c.append(i)
for i in m:
    if i not in n and i!=" ":
        if i not in c:
            c.append(i)            
print(len(c))            