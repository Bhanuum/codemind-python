k=int(input())
for l in range(k):
    a,b=map(int,input().split())
    s=input()
    j=0
    while j<b:
        r=s[:b-j]
        s=r[::-1]+s[b-j:]
        j+=1
    print(s)    
        