n=input().lower()
m=input().lower()
c=[]
for i in n:
    if i in m and i!=" ":
        if i not in c:
            c.append(i)
print(len(c))            