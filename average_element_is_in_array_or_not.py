n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum=sum+i
k=sum//n
for i in a:
    if(i==k):
        print(True)
        break
else:
    print(False)