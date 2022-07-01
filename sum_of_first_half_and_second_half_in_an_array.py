n=int(input())
a=list(map(int,input().split()))
x=n//2
l=r=sum=0
for i in range(x):
    l=l+a[i]
for i in a:
    sum=sum+i
print(l)
print(sum-l)