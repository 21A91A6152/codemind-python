n=int(input())
a=list(map(int,input().split()))
b=[]
p=1
for i in range(n):
    p=p*a[i]
for i in range(n):
    k=p//a[i]
    b.append(k)
print(*b)