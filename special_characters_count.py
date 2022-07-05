n=input()
c=0
p='!@#$^_~./,<>;:"?-\|+=%&*(){}[]`'
for i in n:
    if i in p:
        c+=1
print(c)        