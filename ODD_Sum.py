n=int(input())
a=list(map(int,input().split()))
so=0
for i in a:
    if(i%2==1):
        so=so+i
print(so)