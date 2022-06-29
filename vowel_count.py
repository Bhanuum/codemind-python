n=input()
c=0
for i in n:
    if i  in "aeiouAEIOU":
        c+=1
if c>1:
    print(c)
else:
    print("0")