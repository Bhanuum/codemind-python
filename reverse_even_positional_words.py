s=input()
y=s.split()
p=[]
for i in y:
    p.append(i)
for i in range(0,len(p)):
    if i%2==0:
      print(p[i][::-1],end=" ")
    else:
     print(p[i],end=" ")
      