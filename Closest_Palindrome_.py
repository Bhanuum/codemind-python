n=int(input())
a,b=0,1
i=0
while True:
        if i==n:
            i+=1
        p=str(i)
        k=p[::-1]
        if i==int(k):
            a,b=b,i
            if n<b:
                h=b-n
                g=n-a
                break
        i+=1
if h<g:
         print(b)
elif h>g:
           print(a)
elif h==g:
         print(a,b)
