n=int(input())
a=list(map(int,input().split()))
se=0
for i in a:
    if(i%2==0):
        se=se+i
print(se)