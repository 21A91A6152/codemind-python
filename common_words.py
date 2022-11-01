x=input()
y=input()
x=x.lower()
y=y.lower()
a=list(x.split(" "))
b=list(y.split(" "))
for i in b:
    if i in a:
        print(i,end=" ")