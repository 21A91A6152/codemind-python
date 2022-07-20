n=input()
n=n.lower()
a=list(n.split(" "))
c=0
for i in a:
    temp=i
    if(temp==i[::-1]):
        c+=1
print(c)