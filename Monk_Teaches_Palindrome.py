n=int(input())
for i in range(n):
    k=input()
    j=k[::-1]
    if k==j:
        if len(k)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")