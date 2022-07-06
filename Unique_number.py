m=input()
c=0
for i in m:
  if m.count(i)==1:
      pass
  else:
      c+=1
if c==0:
    print("Unique Number")
else:
    print("Not Unique Number")