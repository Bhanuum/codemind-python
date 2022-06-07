n=int(input())
big=0
while n:
    r=n%10
    if r>big:
        big=r
    n//=10    
print(big)    