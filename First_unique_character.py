s = input().lower()
s = s.replace(" ","")
k=0
for i in s:
    if s.count(i)==1:
        print(i)
        k=1
        break
if k==0:
  print("-1")