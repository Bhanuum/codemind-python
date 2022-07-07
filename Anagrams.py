a=input().lower()
b=input().lower()
c=0
for i in a:
    for j in b:
        if i==j:
            c+=1
if c==len(a):
    print(True)
else:
    print(False)