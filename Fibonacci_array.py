n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(3,len(x)):
    if x[i]==x[i-1]+x[i-2]:
        c+=1
if c+3==n:
    print("yes")
else:
    print("no")