n=input()
p=int(n)**2
m=n[::-1]
m=int(m)
b=m*m
k=str(b)
k=(k[::-1])
if int(k)==p:
    print(True)
else:
    print(False)
    