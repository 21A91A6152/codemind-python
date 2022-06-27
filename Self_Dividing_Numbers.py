a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    c=0
    d=0
    while(i>0):
        r=i%10
        i=i//10
        c+=1
        if(r>0):
            if(temp%r==0):
                d+=1
    if(c==d):
        print(temp,end=' ')
        
        