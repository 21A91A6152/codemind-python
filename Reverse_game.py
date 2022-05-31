n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    sum=0
    while(a[i]):
        j=a[i]%10
        sum=sum*10+j
        a[i]=a[i]//10
    print(sum,end=' ')