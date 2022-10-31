a=input()
b=input()
a=a.lower()
b=b.lower()
x=list(a.split(" "))
y=list(b.split(" "))
c=0
for i in x:
    if i in y:
        c+=1
print(c)