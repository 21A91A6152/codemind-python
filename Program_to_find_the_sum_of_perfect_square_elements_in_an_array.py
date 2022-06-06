def square(a):
    res=0
    if a==1:
        return 1
    for i in range(1,a):
        if i*i==a:
            res=1
            break
    if res==1:
        return 1
    else:
        return 0
a=int(input())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    if square(i)==1:
        sum+=i
print(sum)