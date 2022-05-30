a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
b=[]
d=[]
e=[]
for i in x:
    if i not in b:
        b.append(i)
for k in y:
    if k not in e:
        e.append(k)
for j in b:
    if j not in e:
        d.append(j)
        c+=1
for j in e:
    if j not in b:
        d.append(j)
        c+=1

print(c)

    
    