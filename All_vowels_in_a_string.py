n=input()
a=b=c=d=e=0
for i in n:
    if(i=='a'):
        c+=1
    if(i=='e'):
        a+=1
    if(i=='i'):
        b+=1
    if(i=='o'):
        d+=1
    if(i=='u'):
        e+=1
if(a>0 and b>0 and c>0 and d>0 and e>0):
    print(True)
else:
    print(False)
        
    
        
    