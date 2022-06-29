o=input()
s=o.split()
for i in s:
     p=min(i)
     break
k=s[::-1]
for i in k:
    k=max(i)
    break
print(p,k)