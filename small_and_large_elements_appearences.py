n=input()
m=[]
for i in n:
    if(i!=" "):
        m.append(i)
a=min(m)
b=max(m)
c=0
d=0
for i in n:
    if(i==a):
        c+=1
for j in n:
    if(j==b):
        d+=1
print(a,c,b,d,end=" ")
 
 

        