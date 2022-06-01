n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    sum=0
    sum=sum+a[i]+b[i]
    print(sum,end=' ')