n=int(input())
a=list(map(int,input().split()))
b=[]
sum=0
for i in a:
    if(i%2==0):
        break
    sum=sum+i
print(sum)