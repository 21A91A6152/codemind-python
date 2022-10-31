a=input()
a=a.lower()
x=list(a.split(" "))
for i in x:
    b=i
n=0
y=[]
d=len(x)
for i in b:
    c=0
    for j in x:
        if i in j:
            c+=1
    if(c==d):
        y.append(i)
        n+=1
if(len(y)==0):
    print("-1")
else:
    print(min(y))