n=int(input())
for i in range(n):
    p=i*i+1
    if p==n:
        print("NO")
        break
else:
    print("YES")