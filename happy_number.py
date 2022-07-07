n=int(input())
p=0
while True:
 while n:
    r=n%10
    n//=10
    p+=r**2
 if p==1 or p==7:
        print(True)
        break
 elif p<10:
        print(False)
        break
 else:
        n=p
        p=0