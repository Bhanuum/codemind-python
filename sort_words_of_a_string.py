n=input()
p=n.split()
for i in range(0,len(p)):
    d=list(p[i])
    v="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for k in range(len(d)):
        for g in range(len(d)):
            if d[k]<d[g] and d[k] in v and d[g] in v:
                d[k],d[g]=d[g],d[k]
    d=str(d)
    d=d.replace("[","")
    d=d.replace("]","")
    d=d.replace(",","")
    d=d.replace("'","")
    d=d.replace(" ","")
    print(d,end=" ")