m=input()
p=[0]
s=0
for i in m:
    p.append(int(i))
for j in range(1,len(p)):
    k=p[j]**j
    s+=k
if int(m)==s:
    print(True)
else:
    print(False)