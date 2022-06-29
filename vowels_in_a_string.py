n=input()
k=input()
p=list(n)
g=0
for i in range(len(p)):
    if k==p[i]:
     print(True)
     print(i)
     break
else:
    print(False)
