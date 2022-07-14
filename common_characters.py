m = input().lower()
n = input().lower()
a = ''
for i in m:
    if i in n and i not in a and i!=" ":
        a+=i
a=sorted(a)
a = str(a)
a = a.replace("[","")
a = a.replace("]","")
a = a.replace("'","")
a = a.replace(" ","")
a = a.replace(",","")
if len(a)==0:
    print("-1")
else:
    print(a)