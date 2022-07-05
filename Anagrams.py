n=input().lower()
m=input().lower()
c=0
p=[]
for i in n:
    for j in m:
        if i==j:
            p.append(i)
k=[]            
for i in m:
    for j in n:
        if i==j:
          k.append(i)
if len(p)==len(n) and len(k)==len(m):
  print(True)
else:
    print(False)