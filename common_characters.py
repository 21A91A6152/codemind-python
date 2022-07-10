a=input()
b=input()
c=[]
a=a.lower()
b=b.lower()
for i in a :
    if i in b and i!=' ':
        c.append(i)
c=set(c)
c=sorted(c)
if(len(c)>0):
    for j in c:
        print(j,end='')
else:
    print("-1")