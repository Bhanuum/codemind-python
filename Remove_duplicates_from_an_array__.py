n=input()
k=list(input())
result=[]
for i in k:
    if i not in result:
        result.append(i)
for i in range(0,1):
   print(result[i],end=" ")
for i in range(2,len(result)):
    print(result[i],end=" ")    
