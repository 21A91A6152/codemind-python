n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if(a[i]%2==0):
        b.append(a[i])
for j in range(n):
    if(a[j]%2==1):
        b.append(a[j])
print(*b)
    