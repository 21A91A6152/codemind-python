a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
for i in a:
    if i not in b and i!=' ':
        c.append(i)
for i in b:
    if i not in a and i!=' ':
        c.append(i)  
c=set(c)
c=sorted(c)
for j in c:
    print(j,end='')
