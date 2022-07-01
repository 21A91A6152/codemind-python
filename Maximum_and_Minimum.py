n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    x=0
    if i not in b:
        b.append(i)
        x=a.count(i)
        
        if(x==i):
            c.append(i)
if(len(c)>0):
    print(min(c),max(c),end='')
else:
    print("-1")