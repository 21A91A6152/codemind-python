n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
for i in a:
    if(i<x or i>y):
        c.append(i)
if(len(c)>0):
    print(*c)
else:
    print("-1")