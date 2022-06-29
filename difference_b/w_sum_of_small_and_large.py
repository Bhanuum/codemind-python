o=input()
s=o.split()
p=0
k=0
for i in s:
     p+=ord(min(i))
     k+=ord(max(i))
print(k-p)  
