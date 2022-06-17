s=input()
g=0
for i in s:
    if i.isdigit():
        g+=1
if g>0:        
  print("Contains",g,"digit")
else:
   print("Doesn't contain digit")