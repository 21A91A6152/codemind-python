n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
for i in a:
    if(i>=x and i<=y):
        c.append(i)
if(len(c)>0):
    print(max(c))
else:
    print("-1")
