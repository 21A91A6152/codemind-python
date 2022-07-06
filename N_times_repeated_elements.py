n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
for i in a:
    x=a.count(i)
    if x==k:
        if i not in b:
            b.append(i)
if(len(b)>0):
    print(*b)
else:
    print("-1")