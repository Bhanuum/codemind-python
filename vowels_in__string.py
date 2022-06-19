s=input()
c=0
p=[]
for i in s:
    if i in "AEIOUaeiou":
        if i not in p:
            p.append(i)
for i in p:            
  print(i,end=" ")        
        