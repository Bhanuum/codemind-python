n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in s:
        if i.isdigit():
            c+=1
    if c>0:
        print("Yes")
    else:
        print("No")
