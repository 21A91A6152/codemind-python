n=int(input())
a=list(map(int,input().split()))
if(n%2==0):
    k=1
    for i in range(n):
        x=a[i]
        y=a[n-k]
        print(x,y,end=' ')
        k+=1
        if(k==n//2+1):
            break
else:
    k=1
    for i in range(n):
        x=a[i]
        y=a[n-k]
        if(x==y):
            y=0
        print(x,y,end=' ')
        k+=1
        if(k==n//2+2):
            break
        