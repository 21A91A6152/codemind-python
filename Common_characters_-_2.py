a=input()
a=a.lower()
x=list(a.split(" "))
for i in x:
    b=i
    break
n=0
d=len(x)
for i in b:
    c=0
    for j in x:
        if i in j:
            c+=1
    if(c==d):
        n+=1
print(n)