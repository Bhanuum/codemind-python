n=int(input())
for i in range(1,n+1):
    p=65+n
    for j in range(i,n+1):
        print(chr(p-i),end=" ")
    print()    