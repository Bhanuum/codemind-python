s=input()
p=["a","e","i","o","u"]
a=0
g=0
d=0
f=0
for i in s:
    if i.isdigit():
        a+=1
    elif i==" ":
        g+=1
    elif i in p:
        d+=1
    else:
        f+=1
print("Vowels:",d)
print("Consonants:",f)
print("Digits:",a)
print("White spaces:",g)
        
    