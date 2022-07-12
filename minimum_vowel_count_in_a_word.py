n=input()
b=[]
c=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=="u"):
        c+=1
    if(i==' '):
        b.append(c)
        c=0
b.append(c)
print(min(b))