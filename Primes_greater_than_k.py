def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if isprime(a[i]):
        if(a[i]>=k):
            c+=1
print(c)