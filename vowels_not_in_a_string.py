n=input()
p=" "
k="aeiou"
for i in n:
    if i in "aeiouAEIOU":
        p+=i
c=0        
for i in k:
    if i not in p:
        print(i,end=" ")
        c+=1
if c==0:
    print("0")