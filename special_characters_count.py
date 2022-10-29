n=input()
c=0
x=len(n)
for i in n:
    if(i.isalpha() or i==" "):
        c+=1
print(x-c)