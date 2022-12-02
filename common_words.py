n=input()
n=n.lower()
m=input()
m=m.lower()
x=list(n.split(" "))
y=list(m.split(" "))
for i in y:
    if i in x:
        print(i,end=" ")