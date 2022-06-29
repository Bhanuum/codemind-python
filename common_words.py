n=input()
m=input()
p=n.lower()
k=m.lower()
g=p.split()
h=k.split()
for i in h:
    for j in g:
        if i==j:
            print(i,end=" ")
