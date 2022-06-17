s=input()
v=input()
p=0
c=0
for i in s:
    if v in s:
       p=p+(i.count(v))
       c+=1
if(c>0):
    print(p)
       
else:
        print("-1")
        
    
   