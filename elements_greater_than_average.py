n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
for i in range(n):
    sum=sum+a[i]
k=sum//n
for j in range(n):
    if(a[j]>=k):
        c+=1
print(c)