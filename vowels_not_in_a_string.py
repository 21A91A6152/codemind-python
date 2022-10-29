n=input()
n=n.lower()
a="aeiou"
b=[]
c=0
for i in n:
    if i in a:
        b.append(i)
for i in a:
    if i not in b:
        c+=1
        print(i,end=" ")
if(c==0):
    print("0")