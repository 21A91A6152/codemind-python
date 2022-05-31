n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
    while(a[i]):
        j=a[i]%10
        sum=sum+j
        a[i]=a[i]//10
print(sum)