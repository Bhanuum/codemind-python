n=input()
a="aeiou"
b="AEIOU"
p=[]
f=[]
for i in n:
    if i in a:
      if i not in p:
          p.append(i)
for i in n:
    if i in b:
      if i not in p:
          f.append(i)
if len(p)==5 or len(f)==5:
    print(True)
else:
    print(False)