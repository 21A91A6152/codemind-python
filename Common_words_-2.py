a=input()
b=input()
a=a.lower()
b=b.lower()
x=list(a.split(" "))
y=list(b.split(" "))
c=0
for i in x:
    if i in y:
        if(x.count(i)==1 and y.count(i)==1):
            c+=1
print(c)