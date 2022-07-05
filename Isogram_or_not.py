n=input()
c=[]
for i in n:
    if n.count(i)==1 and i!=" ":
        c.append(i)
if len(c)==len(n):
    print(True)
else:
    print(False)
   