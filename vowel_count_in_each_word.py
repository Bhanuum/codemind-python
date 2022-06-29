n=input()
p=n.split()
for i in p:
    c=0
    for j in i:
      if j in "aeiouAEIOU":
          c+=1
    print(c,end=" ") 