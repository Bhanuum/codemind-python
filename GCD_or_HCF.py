def bha(a,b):
    p=min(a,b)
    while True:
        if a%p==0 and b%p==0:
            return p
        p-=1
a,b=map(int,input().split())
print(bha(a,b))