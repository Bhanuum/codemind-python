n=input().lower()
m=input().lower()
c=""
for i in m:
    if i  in n:
        if i not in c:
          c+=i
for i in n:
    if i in m:
        if i not in c:
         c+=i
p=sorted(c)
p=str(p)
p=p.replace(" ","")
p=p.replace("]","")
p=p.replace("[","")
p=p.replace(",","")
p=p.replace("'","")
if len(c)==0:
    print("-1")
else:
    print(p)
