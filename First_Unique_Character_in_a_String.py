k=input().lower()
n=list(k)
c=0
for i in k:
    if k.count(i)==1:
        c=i
        break
for i in range(len(n)):
    if n[i]==c:
        print(i)
if c==0:
    print("-1")