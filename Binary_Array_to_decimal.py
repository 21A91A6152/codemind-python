n=int(input())
sum=0
a=list(map(int,input().split()))
a.reverse()
for i in range(n):
    sum=sum+(a[i]*pow(2,i))
print(sum)