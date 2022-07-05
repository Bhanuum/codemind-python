n=input()
c=[]
for i in n:
    if i in "aeiouAEIOU":
        if i not in c:
          c.append(i)
print(*c)        