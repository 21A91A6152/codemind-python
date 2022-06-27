n=int(input())
a=list(map(int,input().split()))
c=0
k=0
y=0
for i in a:
    x=a.count(i)
    if(x>=c):
        c=x
for j in a:
    y=a.count(j)
    if(y==c):
        k=j
print(k)
    