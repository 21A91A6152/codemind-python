n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if(i<=n-3):
        x=a[i]
        y=a[i+1]
        z=a[i+2]
        if(x%2==1 and y%2==1 and z%2==1):
            c+=1
print(c)