s=input()
k=s.split()
for i in k:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    print(c,end=" ")        