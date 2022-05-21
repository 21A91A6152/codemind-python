n=int(input())
temp=n
sum=0
while(n):
    i=n%10
    n=n//10
    factorial=1
    for j in range(1,i+1):
        factorial=factorial*j
    sum=sum+factorial
if(sum==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")