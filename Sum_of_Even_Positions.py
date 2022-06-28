n=int(input())
a=list(map(int,input().split()))
se=0
for i in range(n):
    if(i%2==0):
        se=se+a[i]
print(se)