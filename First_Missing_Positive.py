n=int(input())
p=list(map(int,input().split()))
for j in range(1,100):
    if j not in p:
        print(j)
        break