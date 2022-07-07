n=input()
p="aeiou"
k="AEIOU"
c=0
j=0
for i in p:
    if i in n:
        c+=1
for i in k:
    if i in n:
        j+=1
if c==5 or j==5:
    print(True)
else:
    print(False)