n,k=map(int,input().split())
a=list(map(int,input().split()))
m=0
for j in a:
    d=0
    if(j<0):
        j=j*(-1)
    if j==0:
        d=1
    while(j):
        y=j%10
        j=j//10
        d+=1
    if(d==k):
        m+=1
print(m)