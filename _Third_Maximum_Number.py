n=int(input())
a=list(map(int,input().split()))
a=set(a)
x=max(a)
a.remove(x)
if(len(a)>0):
    y=max(a)
    a.remove(y)
    if(len(a)>0):
        z=max(a)
        if(z>0):
            print(z)
    else:
        print(x)
else:
    print(x)