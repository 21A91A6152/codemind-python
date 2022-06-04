n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum=sum+i
k=sum/n
print("{:.2f}".format(k))