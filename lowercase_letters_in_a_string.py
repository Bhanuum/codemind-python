n=input()
c=0
for i in n:
    for j in i:
        if i.islower():
          c+=1
print(c)        