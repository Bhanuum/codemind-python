n=input()
m=n.split()
c=0
k="aeiouAEIOU"
for i in m:
        h=i[0]
        p=i[-1]
        if h in k and p not in k :
            c+=1
print(c)            
        