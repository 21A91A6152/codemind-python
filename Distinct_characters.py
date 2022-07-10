n=input()
n=n.lower()
b=[]
for i in n:
    if n.count(i)==1 and i!=' ':
        b.append(i)
b=sorted(b)
for j in b:
    print(j,end='')