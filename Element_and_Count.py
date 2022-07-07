n=int(input())
a=list(map(int,input().split()))
c=[]
b=[]
d=[]
for i in a:
    if i not in b:
        b.append(i)
        c.append(a.count(i))
for i in range(len(b)):
    d.append(b[i])
    d.append(c[i])
print(*d)