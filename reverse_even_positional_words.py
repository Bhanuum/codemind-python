n=input()
p=n.split()
for i in range(0,len(p)):
    if i%2==0:
        print(p[i][::-1],end=" ")
    else:
        print(p[i],end=" ")