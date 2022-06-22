n=input()
s=input()
p=[]
for i in n:
    p.append(i)
for i in range(len(p)):
    if p[i]==s:
        print(True)
        print(i)
        break
else:
    print(False)
    