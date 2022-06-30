n=int(input())
a=n
p=n*n
a=str(a)
p=str(p)
if p.endswith(a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")