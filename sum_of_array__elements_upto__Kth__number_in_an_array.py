n=int(input())
a=list(map(int,input().split()))
x=int(input())
sum=0
for i in a:
     sum=sum+i
     if(i==x):
         break
print(sum)