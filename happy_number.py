n = int(input())
sum = 0
while True:
    while n!=0:
        sum+=(n%10)**2
        n//=10
    if sum==1 or sum==7:
        print(True)
        break
    elif sum<10:
        print(False)
        break
    else:
        n=sum
        sum=0