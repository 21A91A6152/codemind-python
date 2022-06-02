s=input()
a=len(s)
b=[]
for i in s:
        b.append(s.count(i))
for i in b:
    if i==2:
        print('False')
        break
else:
    print('True')
    
    