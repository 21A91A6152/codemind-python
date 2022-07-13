n=input()
n=n.lower()
v="aeiou"
c=[]
b=[]
for i in n:
    if i in v:
        if i not in b:
            b.append(i)
for i in v:
    if i not in b:
        c.append(i)
if(len(c)>0):
    print(*c)
else:
    print("0")

    
