n=int(input())
x=list(map(int,input().split()))
c=0
d=0
if(x[0]<x[1]):
    for i in range(n-2):
        if(i%2==0):
            if(x[i]<x[i+1] and x[i+1]>x[i+2]):
                c+=1
            else:
                print(-1)
                d+=1
                break
else:
    for i in range(n):
        if(i%2==0):
            if(x[i]>x[i+1] and x[i+1]<x[i+2]):
                c+=1
            else:
                print(-1)
                d+=1
                break
if(d==0):
    print(c)
