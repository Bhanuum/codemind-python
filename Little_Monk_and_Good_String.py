n=input()
a="aeiou"
c=0
k=0
d=""
for i in range(len(n)):
    if n[i] in a:
        c+=1
    if n[i] not in a:
        if k<c:
            k=c
        c=0
if k<c:
    k=c
print(k)