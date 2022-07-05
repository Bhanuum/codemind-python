s1=input().lower()
s2=input().lower()
s1=s1.split()
s2=s2.split()
c=[]
for i in s1:
    for j in s2:
        if i not in c:
            if s1.count(i)==1 and s2.count(j)==1:
              if i==j and i!=" ":
                 c.append(i)
print(len(c))                 
