a = input().lower()
b = input().lower()
a,b = set(a),set(b)
a,b = list(a),list(b)
c = []
for i in range(0,len(a)):
    if a[i] not in b and i!=" ":
        c.append(a[i])
for i in range(0,len(b)):
    if b[i] not in a and i!=" ":
      if b[i] not in c:
        c.append(b[i])
c.sort()
c = str(c)
c = c.replace(",","")
c = c.replace("'","")
c = c.replace("[","")
c = c.replace("]","")
c = c.replace(" ","")
print(c)
