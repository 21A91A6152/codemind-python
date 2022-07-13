n=input()
v="aeiou"
b=[]
c=[]
for i in n:
    if i in v:
        if i not in b:
            b.append(i)
if(len(b)==5):
    print(True)
else:
    print(False)
    