s=input()
m="0"
for i in range(len(s)):
    if ord(s[i])>ord(m):
        m=s[i]
print(m)        
